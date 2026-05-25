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

    product_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(150)
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10,2)
    )

    stock_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    image_url: Mapped[str] = mapped_column(
        String(500),
        default=""
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.category_id")
    )

    brand: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    rating: Mapped[Decimal] = mapped_column(
        Numeric(2,1),
        default=0
    )

    discount: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=text(
            "CURRENT_TIMESTAMP"
        )
    )

    reviews: Mapped[List["Review"]] = relationship(
        back_populates="product"
    )