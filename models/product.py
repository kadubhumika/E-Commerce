from __future__ import annotations  # Required for forward references
from datetime import datetime
from decimal import Decimal
from typing import List, TYPE_CHECKING  # Added TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, text, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

if TYPE_CHECKING:
    from models.review import Review  # Added this block


class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="product"
    )
