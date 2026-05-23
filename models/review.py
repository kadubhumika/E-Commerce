from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base

if TYPE_CHECKING:
    from models.product import Product
    from models.customer import Customer


class Review(Base):
    __tablename__ = "reviews"

    review_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id")
    )

    rating: Mapped[int] = mapped_column(Integer)

    comment: Mapped[str] = mapped_column(String)

    product: Mapped["Product"] = relationship(
        back_populates="reviews"  # Add this to link back to Product.reviews
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="reviews"
    )