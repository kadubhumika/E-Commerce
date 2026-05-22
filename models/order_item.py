from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.order import Order
    from models.product import Product

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    order: Mapped["Order"] = relationship(back_populates="order_items")
    product: Mapped["Product"] = relationship()
