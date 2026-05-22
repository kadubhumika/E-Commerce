from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import *
from models.cart_item import CartItem
from schemas import *
from schemas.cart_item import CartItemCreate


class CartService:
    @staticmethod
    async def view_cart_items(db:AsyncSession,cart_id:int):
        result = await db.execute(select(CartItem).where(CartItem.cart_id==cart_id))
        return result.scalars().all()
    @staticmethod
    async def add_item_to_cart(db:AsyncSession,data:CartItemCreate):
        prod_check = await db.execute(select(Product).where(Product.product_id == data.product_id))
        product = prod_check.scalar_one_or_none()
        if not product or product.stock < data.quantity:
            return None
        existing = await db.execute(
            select(CartItem).where(CartItem.cart_id == data.cart_id, CartItem.product_id == data.product_id)
        )
        cart_item = existing.scalar_one_or_none()
        if cart_item:
            cart_item.quantity += data.quantity
        else:
            cart_item = CartItem(**data.model_dump())
            db.add(cart_item)
        await db.commit()
        await db.refresh(cart_item)
        return cart_item