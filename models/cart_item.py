from sqlalchemy import Column,Integer,ForeignKey

from sqlalchemy.orm import relationship, Mapped, mapped_column

from models import Product
from models.base import Base
from models.cart import Cart


class CartItem(Base):
    __tablename__ = "cart_items"
    cart_item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.cart_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    quantity: Mapped[int] = mapped_column(Integer)

    cart: Mapped[Cart] = relationship(back_populates="cart_items")
    product: Mapped[Product] = relationship()
