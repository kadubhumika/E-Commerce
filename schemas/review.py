from pydantic import Field

from schemas.base import BaseSchema

class ReviewCreate(BaseSchema):
    product_id: int
    customer_id: int
    rating: int = Field(
        ge=1,
        le=5
    )
    comment: str

class ReviewUpdate(BaseSchema):
    rating: int = Field(
        ge=1,
        le=5
    )
    comment: str | None = None

class ReviewResponse(BaseSchema):
    review_id: int
    product_id: int
    customer_id: int
    rating: int
    comment: str