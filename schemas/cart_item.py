from pydantic import Field

from schemas.base import BaseSchema

class CartItemCreate(BaseSchema):
    cart_id: int
    product_id: int
    quantity: int = Field(
        gt=0
    )

class CartItemUpdate(BaseSchema):
    quantity: int = Field(
        gt=0
    )

class CartItemResponse(BaseSchema):
    cart_item_id: int
    cart_id: int
    product_id: int
    quantity: int = Field(
        gt=0
    )