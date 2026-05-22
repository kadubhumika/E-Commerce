from decimal import Decimal
from schemas.base import BaseSchema

class OrderItemCreate(BaseSchema):
    order_id: int
    product_id: int
    quantity: int
    price: Decimal

class OrderItemResponse(BaseSchema):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    price: Decimal
