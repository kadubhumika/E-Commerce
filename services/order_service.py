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
            if product.stock_quantity < item.quantity:
                return None

            product.stock_quantity -= item.quantity

            # Prep permanent order record item snapshot
            order_items_to_create.append(
                OrderItem(product_id=item.product_id, quantity=item.quantity, price=product.price)
            )
            customer_result = await db.execute(
                select(Customer).where(
                    Customer.customer_id == customer_id
                )
            )

            customer = customer_result.scalar_one_or_none()
            shipping_address = (
                f"{customer.address}, "
                f"{customer.city}, "
                f"{customer.state}, "
                f"{customer.country}, "
                f"{customer.pincode}"
            )
        new_order = Order(
            customer_id=customer_id,
            total_amount=total_price,
            status="PENDING",
            payment_method=payment_method,
            shipping_address=shipping_address
        )
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

    @staticmethod
    async def update_order_status(
            db: AsyncSession,
            order_id: int,
            status: str
    ):

        result = await db.execute(
            select(Order).where(
                Order.order_id == order_id
            )
        )

        order = result.scalar_one_or_none()

        if not order:
            return None

        order.status = status

        await db.commit()
        await db.refresh(order)

        return order

    @staticmethod
    async def get_orders(
            db: AsyncSession,
            customer_id: int
    ):

        result = await db.execute(
            select(Order).where(
                Order.customer_id == customer_id
            )
        )

        return result.scalars().all()
