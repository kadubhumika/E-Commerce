from schemas.base import BaseSchema

class CartItemCreate(BaseSchema):
    cart_id: int
    product_id: int
    quantity: int

class CartItemUpdate(BaseSchema):
    quantity: int | None = None

class CartItemResponse(BaseSchema):
    cart_item_id: int
    cart_id: int
    product_id: int
    quantity: int