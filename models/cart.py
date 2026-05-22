from typing import List

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models import Customer
from models.base import Base
from models.cart_item import CartItem


class Cart(Base):
    __tablename__ = "carts"
    cart_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))

    customer: Mapped[Customer] = relationship(back_populates="cart")
    cart_items: Mapped[List[CartItem]] = relationship(back_populates="cart")