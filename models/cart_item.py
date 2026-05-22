from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.cart import Cart
    from models.product import Product

class CartItem(Base):
    __tablename__ = "cart_items"

    cart_item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.cart_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    quantity: Mapped[int] = mapped_column(Integer)

    # String references break the runtime imports loop cleanly!
    cart: Mapped["Cart"] = relationship(back_populates="cart_items")
    product: Mapped["Product"] = relationship()
