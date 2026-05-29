"""
Расширенный демо-сидер для кофейни «Кофеёчек».

Создаёт:
  - 4 категории
  - ~30 позиций меню
  - 4 клиента + admin
  - 12 заказов с разными статусами
  - 18 отзывов
"""
import asyncio
import os
import random
import sys
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

import httpx
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings
from app.core.security import get_password_hash
from app.models.category import Category
from app.models.menu_item import MenuItem
from app.models.order import Order, OrderStatus
from app.models.order_item import OrderItem
from app.models.review import Review
from app.models.role import Role
from app.models.user import User


CATEGORIES = [
    {"name": "Кофе", "description": "Ароматные кофейные напитки на любой вкус"},
    {"name": "Чай", "description": "Классические чаи и травяные сборы"},
    {"name": "Десерты", "description": "Сладкие угощения к напиткам"},
    {"name": "Завтраки", "description": "Сытные завтраки для бодрого начала дня"},
]

MENU = [
    # Кофе
    ("Эспрессо", "Кофе", 120, 30,
     "Классический крепкий кофе — основа всех кофейных напитков",
     "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=400", "espresso.jpg"),
    ("Двойной эспрессо", "Кофе", 160, 60,
     "Двойная порция эспрессо для тех, кому нужна максимальная бодрость",
     "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=400", "double_espresso.jpg"),
    ("Американо", "Кофе", 150, 200,
     "Эспрессо, разбавленный горячей водой",
     "https://images.unsplash.com/photo-1521302080334-4bebac2763a6?w=400", "americano.jpg"),
    ("Капучино", "Кофе", 180, 200,
     "Эспрессо с нежной молочной пенкой",
     "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400", "cappuccino.jpg"),
    ("Латте", "Кофе", 200, 300,
     "Мягкий кофейный напиток с большим количеством молока",
     "https://images.unsplash.com/photo-1561882468-9110e03e0f78?w=400", "latte.jpg"),
    ("Раф классический", "Кофе", 220, 300,
     "Взбитый эспрессо с ванильными сливками — наш фирменный напиток",
     "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400", "raf_classic.jpg"),
    ("Раф лавандовый", "Кофе", 240, 300,
     "Раф с тонким ароматом лаванды и мёда",
     "https://images.unsplash.com/photo-1572286258217-215cf8e8c5fa?w=400", "raf_lavender.jpg"),
    ("Флэт-уайт", "Кофе", 200, 220,
     "Двойной эспрессо с молочной микропеной",
     "https://images.unsplash.com/photo-1507133750040-4a8f57021571?w=400", "flat_white.jpg"),
    ("Мокко", "Кофе", 230, 300,
     "Кофейно-шоколадный коктейль со взбитыми сливками",
     "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=400", "mocha.jpg"),
    ("Кофе по-восточному", "Кофе", 180, 80,
     "Турецкий кофе на песке с кардамоном",
     "https://images.unsplash.com/photo-1565881606991-789c2962a5a3?w=400", "turkish_coffee.jpg"),
    ("Айс-латте", "Кофе", 220, 300,
     "Холодный латте со льдом — освежает и бодрит",
     "https://images.unsplash.com/photo-1517959105821-eaf2591984ca?w=400", "iced_latte.jpg"),
    ("Глясе", "Кофе", 250, 300,
     "Холодный кофе с шариком ванильного мороженого",
     "https://images.unsplash.com/photo-1497636577773-f1231844b336?w=400", "glace.jpg"),
    # Чай
    ("Чай с бергамотом", "Чай", 130, 300,
     "Классический Earl Grey с тонким ароматом бергамота",
     "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=400", "tea_bergamot.jpg"),
    ("Зелёный чай Сенча", "Чай", 140, 300,
     "Нежный зелёный чай Сенча из Японии",
     "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400", "tea_sencha.jpg"),
    ("Имбирный чай с лимоном", "Чай", 160, 300,
     "Согревающий напиток с свежим имбирём, лимоном и мёдом",
     "https://images.unsplash.com/photo-1597481499750-3e6b22637e12?w=400", "tea_ginger.jpg"),
    ("Облепиховый чай", "Чай", 180, 300,
     "Кисло-сладкий напиток из свежей облепихи",
     "https://images.unsplash.com/photo-1567922045116-2a00fae2ed03?w=400", "tea_seabuckthorn.jpg"),
    ("Марокканская мята", "Чай", 150, 300,
     "Зелёный чай со свежей мятой",
     "https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=400", "tea_mint.jpg"),
    ("Фруктовый чай Малина-Лайм", "Чай", 170, 300,
     "Освежающий фруктовый микс с сиропом малины",
     "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=400", "tea_raspberry.jpg"),
    # Десерты
    ("Чизкейк Нью-Йорк", "Десерты", 280, 150,
     "Классический сливочный чизкейк с ягодным соусом",
     "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=400", "cheesecake.jpg"),
    ("Тирамису", "Десерты", 290, 130,
     "Итальянский десерт из маскарпоне и кофейных бисквитов",
     "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400", "tiramisu.jpg"),
    ("Брауни шоколадный", "Десерты", 220, 120,
     "Тёплый шоколадный брауни с шариком ванильного мороженого",
     "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400", "brownie.jpg"),
    ("Круассан с маслом", "Десерты", 120, 80,
     "Свежеиспечённый слоёный круассан — хрустящий снаружи, нежный внутри",
     "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400", "croissant_butter.jpg"),
    ("Круассан с шоколадом", "Десерты", 150, 90,
     "Слоёный круассан с тёмным бельгийским шоколадом",
     "https://images.unsplash.com/photo-1623334044303-241021148842?w=400", "croissant_choco.jpg"),
    ("Маффин черничный", "Десерты", 160, 100,
     "Нежный кекс со свежей черникой",
     "https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=400", "muffin_blueberry.jpg"),
    ("Эклер ванильный", "Десерты", 180, 80,
     "Заварное пирожное с ванильным кремом",
     "https://images.unsplash.com/photo-1607920591413-e2d72ed3fa42?w=400", "eclair.jpg"),
    # Завтраки
    ("Сырники со сметаной", "Завтраки", 250, 250,
     "Пышные творожные сырники со сметаной и вареньем",
     "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400", "syrniki.jpg"),
    ("Овсяная каша с ягодами", "Завтраки", 180, 300,
     "Тёплая овсяная каша с сезонными ягодами и мёдом",
     "https://images.unsplash.com/photo-1495214783159-3503fd1b572d?w=400", "oatmeal.jpg"),
    ("Гранола с йогуртом и фруктами", "Завтраки", 220, 280,
     "Хрустящая домашняя гранола, греческий йогурт, сезонные фрукты",
     "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400", "granola.jpg"),
    ("Сэндвич с тунцом", "Завтраки", 290, 200,
     "Тостовый сэндвич с тунцом, яйцом, рукколой и томатами",
     "https://images.unsplash.com/photo-1559054663-e9d1c4e98a1c?w=400", "sandwich_tuna.jpg"),
    ("Авокадо-тост", "Завтраки", 320, 220,
     "Зерновой хлеб, гуакамоле, яйцо пашот, кунжут",
     "https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=400", "avocado_toast.jpg"),
    ("Омлет с овощами", "Завтраки", 240, 250,
     "Воздушный омлет с томатами, перцем и зеленью",
     "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400", "omelette.jpg"),
    ("Блинчики со сгущёнкой", "Завтраки", 200, 220,
     "Тонкие блинчики с домашней сгущёнкой",
     "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400", "blini.jpg"),
]

CLIENTS = [
    ("Иван Петров", "ivan@example.com"),
    ("Анна Смирнова", "anna@example.com"),
    ("Сергей Иванов", "sergey@example.com"),
    ("Мария Кузнецова", "maria@example.com"),
]

REVIEW_TEXTS = [
    "Очень вкусный раф, точно вернусь!",
    "Капучино идеальный, пенка как в Италии.",
    "Чизкейк просто тает во рту, спасибо!",
    "Уютная атмосфера, приятная музыка, рекомендую.",
    "Латте на овсяном молоке отличный, для веганов то что надо.",
    "Сырники нежные, сметана домашняя — топ.",
    "Брал кофе с собой — всё аккуратно, ничего не пролилось.",
    "Бариста подсказал интересный напиток с лавандой — попробую ещё.",
    "Цены адекватные, качество стабильное.",
    "Чай с облепихой шикарный, грею душу зимой.",
    "Тирамису как в Италии, прям не ожидал.",
    "Авокадо-тост свежий, яйцо пашот идеально приготовлено.",
    "Кофе тут лучший в районе, проверено.",
    "Эклер прекрасный, не приторный, крем нежный.",
    "Завтраки вкусные и сытные, цена/качество отличная.",
    "Бариста улыбается, помнит постоянных — приятно.",
    "Маффин с черникой свежий, ягод много.",
    "Атмосфера для работы и встречи отлично подходит, есть розетки и Wi-Fi.",
]


IMAGES_DIR = Path(__file__).parent / "static" / "images"


async def download_image(client: httpx.AsyncClient, url: str, filename: str) -> str:
    """Download image to local static dir; return local URL or original on failure."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    dest = IMAGES_DIR / filename
    if dest.exists():
        return f"/static/images/{filename}"
    try:
        r = await client.get(url, follow_redirects=True, timeout=20)
        if r.status_code == 200:
            dest.write_bytes(r.content)
            print(f"[seed] скачано: {filename}")
            return f"/static/images/{filename}"
    except Exception as exc:
        print(f"[seed] не удалось скачать {filename}: {exc}")
    return url


async def already_seeded(session) -> bool:
    n = await session.scalar(select(func.count()).select_from(MenuItem))
    return (n or 0) > 15


async def seed() -> None:
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=False,
        connect_args={"check_same_thread": False},
    )
    AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with AsyncSessionLocal() as session:
        is_seeded = await already_seeded(session)

        # Roles
        result = await session.execute(select(Role))
        existing_roles = {r.name: r for r in result.scalars().all()}
        admin_role = existing_roles.get("admin")
        if not admin_role:
            admin_role = Role(name="admin")
            session.add(admin_role)
            await session.flush()
        customer_role = existing_roles.get("customer")
        if not customer_role:
            customer_role = Role(name="customer")
            session.add(customer_role)
            await session.flush()

        # Admin
        result = await session.execute(select(User).where(User.email == "admin@coffeecheck.ru"))
        admin_user = result.scalar_one_or_none()
        if not admin_user:
            admin_user = User(
                full_name="Администратор",
                email="admin@coffeecheck.ru",
                hashed_password=get_password_hash("admin12345"),
                role_id=admin_role.id,
                is_active=True,
            )
            session.add(admin_user)
            await session.flush()

        # Categories — нужны до создания позиций меню
        cat_map: dict[str, Category] = {}
        result = await session.execute(select(Category))
        for cat in result.scalars().all():
            cat_map[cat.name] = cat
        for cat_data in CATEGORIES:
            if cat_data["name"] not in cat_map:
                cat = Category(**cat_data)
                session.add(cat)
                await session.flush()
                cat_map[cat.name] = cat

        # Menu — скачиваем изображения локально, обновляем/создаём записи
        result = await session.execute(select(MenuItem))
        existing_items = {m.name: m for m in result.scalars().all()}
        all_items: list[MenuItem] = list(existing_items.values())
        async with httpx.AsyncClient() as http_client:
            for name, cat_name, price, grams, desc, orig_url, img_filename in MENU:
                local_url = await download_image(http_client, orig_url, img_filename)
                if name in existing_items:
                    mi = existing_items[name]
                    if mi.image_url and "unsplash.com" in mi.image_url:
                        mi.image_url = local_url
                    continue
                cat = cat_map[cat_name]
                mi = MenuItem(
                    name=name,
                    description=desc,
                    price=Decimal(str(price)),
                    weight_grams=grams,
                    image_url=local_url,
                    category_id=cat.id,
                    is_active=True,
                    is_available=True,
                )
                session.add(mi)
                await session.flush()
                all_items.append(mi)

        if is_seeded:
            await session.commit()
            print("[seed] изображения обновлены (база уже была засеяна)")
            await engine.dispose()
            return

        # Clients
        clients: list[User] = []
        for full_name, email in CLIENTS:
            result = await session.execute(select(User).where(User.email == email))
            u = result.scalar_one_or_none()
            if not u:
                u = User(
                    full_name=full_name,
                    email=email,
                    hashed_password=get_password_hash("user12345"),
                    role_id=customer_role.id,
                    is_active=True,
                )
                session.add(u)
                await session.flush()
            clients.append(u)

        # Orders
        rng = random.Random(42)
        statuses = [
            OrderStatus.COMPLETED, OrderStatus.COMPLETED, OrderStatus.COMPLETED,
            OrderStatus.READY, OrderStatus.READY,
            OrderStatus.PREPARING, OrderStatus.PREPARING,
            OrderStatus.CONFIRMED,
            OrderStatus.NEW, OrderStatus.NEW,
            OrderStatus.CANCELLED, OrderStatus.COMPLETED,
        ]
        for i, status in enumerate(statuses):
            client = clients[i % len(clients)]
            n_items = rng.randint(1, 3)
            picks = rng.sample(all_items, n_items)
            order = Order(
                user_id=client.id,
                status=status,
                total_amount=Decimal("0"),
                delivery_type=rng.choice(["pickup", "delivery"]),
                delivery_address="г. Москва, ул. Примерная, д. 1" if rng.random() < 0.5 else None,
                created_at=datetime.utcnow() - timedelta(days=rng.randint(0, 30)),
            )
            session.add(order)
            await session.flush()
            total = Decimal("0")
            for mi in picks:
                qty = rng.randint(1, 2)
                subtotal = Decimal(str(mi.price)) * qty
                total += subtotal
                session.add(OrderItem(
                    order_id=order.id,
                    menu_item_id=mi.id,
                    item_name=mi.name,
                    price=mi.price,
                    quantity=qty,
                    subtotal=subtotal,
                ))
            order.total_amount = total

        # Reviews
        for i, text in enumerate(REVIEW_TEXTS):
            client = clients[i % len(clients)]
            mi = all_items[i % len(all_items)]
            session.add(Review(
                user_id=client.id,
                menu_item_id=mi.id,
                rating=rng.choice([4, 5, 5, 5, 5]),
                text=text,
            ))

        await session.commit()
        print(f"[seed] cafe готово: {len(MENU)} позиций, {len(CLIENTS)} клиентов, "
              f"{len(statuses)} заказов, {len(REVIEW_TEXTS)} отзывов")

    await engine.dispose()


if __name__ == "__main__":
    print("Starting seed for Кофеёчек...")
    asyncio.run(seed())
