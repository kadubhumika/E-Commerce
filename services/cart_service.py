from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import *
from models.cart_item import CartItem
from schemas import *
from schemas.cart_item import CartItemCreate


class CartService:
    @staticmethod
    async def view_cart_items(db: AsyncSession, cart_id: int):

        result = await db.execute(
            select(CartItem, Product)
            .join(Product, CartItem.product_id == Product.product_id)
            .where(CartItem.cart_id == cart_id)
        )

        rows = result.all()

        return [
            {
                "cart_item_id": cart_item.cart_item_id,
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "image_url": product.image_url,
                "quantity": cart_item.quantity
            }
            for cart_item, product in rows
        ]
    @staticmethod
    async def add_item_to_cart(db:AsyncSession,cart_id:int, data:CartItemCreate):
        prod_check = await db.execute(select(Product).where(Product.product_id == data.product_id))
        product = prod_check.scalar_one_or_none()
        if not product or product.stock_quantity < data.quantity:
            return None
        existing = await db.execute(
            select(CartItem).where(CartItem.cart_id == cart_id, CartItem.product_id == data.product_id)
        )
        cart_item = existing.scalar_one_or_none()
        if cart_item:
            cart_item.quantity += data.quantity
        else:
            cart_item = CartItem(
                cart_id=cart_id,
                product_id=data.product_id,
                quantity=data.quantity
            )
            db.add(cart_item)
        await db.commit()
        await db.refresh(cart_item)
        return cart_item

    @staticmethod
    async def update_item_quantity(
            db: AsyncSession,
            cart_item_id: int,
            quantity: int
    ):
        result = await db.execute(
            select(CartItem)
            .where(CartItem.cart_item_id == cart_item_id)
        )

        item = result.scalar_one_or_none()

        if not item:
            return None

        item.quantity = quantity

        await db.commit()
        await db.refresh(item)

        return item

    @staticmethod
    async def remove_item(
            db: AsyncSession,
            cart_item_id: int
    ):

        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_item_id == cart_item_id
            )
        )

        item = result.scalar_one_or_none()

        if not item:
            return None

        await db.delete(item)

        await db.commit()

        return True