from typing import List, TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.customer import Customer
    from models.cart_item import CartItem


class Cart(Base):
    __tablename__ = "carts"

    cart_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))

    # Pass the class names as strings ("Customer", "CartItem") to prevent the loop crash!
    customer: Mapped["Customer"] = relationship(back_populates="cart")
    cart_items: Mapped[List["CartItem"]] = relationship(back_populates="cart")
