from decimal import Decimal

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base
from models.order import Order


class Payment(Base):
    __tablename__ = "payments"
    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))  # Added amount column to match schema
    payment_method: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="pending")  # Renamed payment_status -> status

    order: Mapped[Order] = relationship(back_populates="payment")