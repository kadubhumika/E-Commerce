from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    TIMESTAMP,
    text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from models.base import Base

class Category(Base):
    __tablename__ = "categories"
    category_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True) # Allowed Null to match minimal schema
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))