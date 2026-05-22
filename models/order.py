from decimal import Decimal

from sqlalchemy import Column, Integer, Float, String, ForeignKey, Numeric

from sqlalchemy.orm import relationship, Mapped, mapped_column

from models import Customer
from models.base import Base


class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))  # Changed to Numeric
    status: Mapped[str] = mapped_column(String, default="pending")

    customer: Mapped[Customer] = relationship(back_populates="orders")
    order_items: Mapped[List[OrderItem]] = relationship(back_populates="order")
    payment: Mapped[Payment | None] = relationship(back_populates="order")