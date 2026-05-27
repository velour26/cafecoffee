from fastapi import APIRouter

from app.api.v1.endpoints import (
    ai_advisor,
    auth,
    cart,
    categories,
    contact_messages,
    favorites,
    menu_items,
    orders,
    reviews,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
api_router.include_router(menu_items.router, prefix="/menu-items", tags=["Menu Items"])
api_router.include_router(cart.router, prefix="/cart", tags=["Cart"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])
api_router.include_router(ai_advisor.router, prefix="/ai", tags=["AI"])
api_router.include_router(contact_messages.router, prefix="/contact-messages", tags=["Contact"])
