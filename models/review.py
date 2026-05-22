from sqlalchemy import Column, Integer, String, ForeignKey, Float

from sqlalchemy.orm import relationship, Mapped, mapped_column

from models import Product, Customer
from models.base import Base


class Review(Base):
    __tablename__ = 'reviews'
    review_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String)

    product: Mapped[Product] = relationship()
    customer: Mapped[Customer] = relationship(back_populates="reviews")
