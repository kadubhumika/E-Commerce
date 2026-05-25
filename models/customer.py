from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

if TYPE_CHECKING:
    from models.auth_user import AuthUser
    from models.cart import Cart
    from models.order import Order
    from models.review import Review   # ← ADD THIS


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("auth_users.id"))
    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    address: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    state: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    country: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    pincode: Mapped[str] = mapped_column(
        String(20),
        default=""
    )

    profile_image: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    auth_user: Mapped["AuthUser"] = relationship(
        back_populates="customer"
    )

    cart: Mapped[Optional["Cart"]] = relationship(
        back_populates="customer"
    )

    orders: Mapped[List["Order"]] = relationship(
        back_populates="customer"
    )

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="customer"
    )