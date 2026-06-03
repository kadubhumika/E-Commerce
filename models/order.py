from decimal import Decimal
from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

# Cleanly separate type checking to prevent circular loops
if TYPE_CHECKING:
    from models.customer import Customer
    from models.order_item import OrderItem
    from models.payment import Payment


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))
    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING"
    )

    payment_method: Mapped[str] = mapped_column(
        String(50)
    )

    shipping_address: Mapped[str] = mapped_column(
        String(500)
    )


    customer: Mapped["Customer"] = relationship(back_populates="orders")
    order_items: Mapped[List["OrderItem"]] = relationship(back_populates="order")
    from typing import Optional
    payment: Mapped[Optional["Payment"]] = relationship(back_populates="order")

