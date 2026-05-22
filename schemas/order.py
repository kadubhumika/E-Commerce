from decimal import Decimal
from schemas.base import BaseSchema

class OrderCreate(BaseSchema):
    customer_id: int

class OrderResponse(BaseSchema):
    order_id: int
    customer_id: int
    total_price: Decimal
    status: str