from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Integer,
    String,
    Float,
    ForeignKey,
    TIMESTAMP,
    text, Numeric
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from models.base import Base

class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2)) # Changed from Float to Numeric for precise currency
    stock: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))