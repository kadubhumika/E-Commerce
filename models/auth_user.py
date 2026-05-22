from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING # Keep this!

from sqlalchemy import Integer, String, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

# This prevents the circular loop!
if TYPE_CHECKING:
    from models.customer import Customer

class AuthUser(Base):
    __tablename__ = "auth_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), default="customer")
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    customer: Mapped["Customer"] = relationship(back_populates="auth_user")
