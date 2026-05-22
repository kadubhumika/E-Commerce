from schemas.base import BaseSchema

class CartCreate(BaseSchema):
    customer_id: int

class CartResponse(BaseSchema):
    cart_id: int
    customer_id: int