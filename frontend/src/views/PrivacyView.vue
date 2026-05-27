<template>
  <div style="background:#fff">

    <section style="background:#0a0a0a">
      <div class="max-w-4xl mx-auto px-6 py-20">
        <p class="text-xs font-bold uppercase tracking-[0.4em] mb-5" style="color:#c1ce56">Документы</p>
        <h1 class="font-black leading-tight mb-5" style="font-size:clamp(2rem,5vw,3.5rem);color:#fff">
          Политика<br>конфиденциальности
        </h1>
        <p class="text-sm" style="color:#555">Последнее обновление: 1 января 2026 года</p>
      </div>
    </section>

    <div class="max-w-4xl mx-auto px-6 py-16">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-12">

        <aside class="hidden lg:block">
          <div class="sticky top-24">
            <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#c1ce56">Содержание</p>
            <nav class="flex flex-col gap-1">
              <a
                v-for="section in sections"
                :key="section.id"
                :href="`#${section.id}`"
                class="text-sm py-1.5 transition-colors block"
                style="color:#bbb;border-left:2px solid #f0f0f0;padding-left:12px"
                @mouseenter="e => { e.currentTarget.style.color='#0a0a0a'; e.currentTarget.style.borderColor='#c1ce56' }"
                @mouseleave="e => { e.currentTarget.style.color='#bbb'; e.currentTarget.style.borderColor='#f0f0f0' }"
              >{{ section.title }}</a>
            </nav>
          </div>
        </aside>

        <article class="lg:col-span-3">
          <div class="flex flex-col gap-12">

            <section v-for="section in sections" :key="section.id" :id="section.id">
              <div class="flex items-center gap-4 mb-6">
                <span class="text-xs font-black px-2 py-1" style="background:#c1ce56;color:#0a0a0a">{{ String(section.n).padStart(2,'0') }}</span>
                <h2 class="font-black text-xl" style="color:#0a0a0a">{{ section.title }}</h2>
              </div>
              <div class="flex flex-col gap-4" style="color:#555;font-size:0.9375rem;line-height:1.8">
                <p v-for="(para, i) in section.content" :key="i" v-html="para"></p>
              </div>

              <ul v-if="section.items" class="mt-4 flex flex-col gap-3">
                <li
                  v-for="item in section.items"
                  :key="item"
                  class="flex items-start gap-3 text-sm"
                  style="color:#555;line-height:1.7"
                >
                  <span class="w-1.5 h-1.5 rounded-full mt-2 shrink-0" style="background:#c1ce56"></span>
                  {{ item }}
                </li>
              </ul>
            </section>

          </div>
        </article>

      </div>
    </div>

    <section style="background:#f5f5f3;border-top:1px solid #f0f0f0">
      <div class="max-w-4xl mx-auto px-6 py-14 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
        <div>
          <p class="font-black text-lg mb-1" style="color:#0a0a0a">Есть вопросы?</p>
          <p class="text-sm" style="color:#888">Напишите нам по поводу ваших персональных данных</p>
        </div>
        <RouterLink
          to="/contacts"
          class="flex items-center gap-3 px-8 py-3 text-xs font-bold uppercase tracking-widest shrink-0 transition-opacity hover:opacity-80"
          style="background:#0a0a0a;color:#fff"
        >
          Написать нам
        </RouterLink>
      </div>
    </section>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const sections = [
  {
    n: 1,
    id: 'general',
    title: 'Общие положения',
    content: [
      'Настоящая политика конфиденциальности определяет порядок обработки и защиты персональных данных пользователей сайта и мобильного приложения «Кофеёчек».',
      'Используя сервисы «Кофеёчек», вы соглашаетесь с условиями данной политики. Если вы не согласны с её условиями, пожалуйста, не используйте наши сервисы.',
    ],
  },
  {
    n: 2,
    id: 'data-collected',
    title: 'Какие данные мы собираем',
    content: [
      'Мы собираем только те данные, которые необходимы для предоставления наших услуг:',
    ],
    items: [
      'Имя и фамилия — для персонализации заказов и обращений',
      'Адрес электронной почты — для входа в аккаунт и уведомлений',
      'Номер телефона — для связи при доставке (необязательно)',
      'Адрес доставки — только при оформлении заказа с доставкой',
      'История заказов — для отображения в личном кабинете',
      'Оценки и отзывы — публикуются с указанием имени пользователя',
    ],
  },
  {
    n: 3,
    id: 'usage',
    title: 'Как мы используем данные',
    content: [
      'Собранные данные используются исключительно для следующих целей:',
    ],
    items: [
      'Создание и управление учётной записью пользователя',
      'Обработка и доставка заказов',
      'Отправка уведомлений о статусе заказа',
      'Улучшение качества сервиса на основе обратной связи',
      'Связь с пользователем по его запросу',
    ],
  },
  {
    n: 4,
    id: 'storage',
    title: 'Хранение и защита данных',
    content: [
      'Все данные хранятся на защищённых серверах с использованием современных методов шифрования. Мы применяем SSL/TLS для защиты передачи данных между вашим устройством и нашими серверами.',
      'Пароли хранятся в хешированном виде — мы не имеем доступа к вашему исходному паролю. Доступ к персональным данным имеют только сотрудники, которым он необходим для выполнения рабочих задач.',
      'Мы храним данные в течение срока действия вашего аккаунта. После удаления аккаунта данные уничтожаются в течение 30 дней.',
    ],
  },
  {
    n: 5,
    id: 'third-parties',
    title: 'Передача третьим лицам',
    content: [
      'Мы не продаём, не сдаём в аренду и не передаём ваши персональные данные третьим лицам без вашего явного согласия, за исключением следующих случаев:',
    ],
    items: [
      'Служба доставки — адрес и контактный телефон для выполнения заказа',
      'Платёжные системы — при оплате онлайн (данные карты обрабатываются платёжным провайдером)',
      'Требование закона — при получении законного запроса от уполномоченных органов',
    ],
  },
  {
    n: 6,
    id: 'cookies',
    title: 'Cookies и аналитика',
    content: [
      'Мы используем cookies для обеспечения работы сайта: хранения токена авторизации и настроек. Мы не используем cookies для отслеживания поведения пользователей в рекламных целях.',
      'Вы можете отключить cookies в настройках браузера, однако это может повлиять на работу некоторых функций сайта.',
    ],
  },
  {
    n: 7,
    id: 'rights',
    title: 'Ваши права',
    content: [
      'В соответствии с законодательством о персональных данных вы имеете право:',
    ],
    items: [
      'Получить информацию о том, какие данные о вас хранятся',
      'Исправить неточные или устаревшие данные через личный кабинет',
      'Запросить удаление своих данных, написав нам на hello@coffeechek.ru',
      'Отозвать согласие на обработку данных в любой момент',
      'Подать жалобу в Роскомнадзор, если вы считаете, что ваши права нарушены',
    ],
  },
  {
    n: 8,
    id: 'contact',
    title: 'Контакты по вопросам данных',
    content: [
      'Если у вас есть вопросы, связанные с обработкой ваших персональных данных, или вы хотите воспользоваться своими правами, свяжитесь с нами:',
      '<strong style="color:#0a0a0a">Email:</strong> hello@coffeechek.ru<br><strong style="color:#0a0a0a">Телефон:</strong> +7 (999) 000-12-34<br><strong style="color:#0a0a0a">Адрес:</strong> ул. Кофейная, 42',
      'Мы обязуемся ответить на ваш запрос в течение 5 рабочих дней.',
    ],
  },
]
</script>
