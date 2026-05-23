from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from models import *
from decimal import Decimal

from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment


class OrderService:
    @staticmethod
    async def checkout_cart(db: AsyncSession, customer_id:int,payment_method:str):
        cart_result = await db.execute(
            select(Cart).where(Cart.customer_id == customer_id).options(selectinload(Cart.cart_items))
        )
        cart = cart_result.scalar_one_or_none()
        if not cart or not cart.cart_items:
            return None
        total_price = Decimal("0.00")
        order_items_to_create = []
        for item in cart.cart_items:
            prod_result = await db.execute(
                select(Product).where(
                    Product.product_id == item.product_id
                )
            )

            product = prod_result.scalar_one_or_none()
            line_price = product.price * item.quantity
            total_price += line_price
            product.stock -= item.quantity

            # Prep permanent order record item snapshot
            order_items_to_create.append(
                OrderItem(product_id=item.product_id, quantity=item.quantity, price=product.price)
            )
        new_order = Order(customer_id=customer_id, total_price=total_price, status="pending")
        db.add(new_order)
        await db.flush()

        for order_item in order_items_to_create:
            order_item.order_id = new_order.order_id
            db.add(order_item)

        new_payment = Payment(
            order_id=new_order.order_id,
            amount=total_price,
            payment_method=payment_method,
            status="pending"
        )
        db.add(new_payment)

        for item in cart.cart_items:
            await db.delete(item)

        await db.commit()
        await db.refresh(new_order)
        return new_order
