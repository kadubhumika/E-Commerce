from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.order import Order


class Payment(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    payment_method: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, default="pending")


    order: Mapped["Order"] = relationship(back_populates="payment")
