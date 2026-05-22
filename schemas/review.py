from schemas.base import BaseSchema

class ReviewCreate(BaseSchema):
    product_id: int
    customer_id: int
    rating: int
    comment: str

class ReviewUpdate(BaseSchema):
    rating: int | None = None
    comment: str | None = None

class ReviewResponse(BaseSchema):
    review_id: int
    product_id: int
    customer_id: int
    rating: int
    comment: str