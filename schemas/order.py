from decimal import Decimal
from schemas.base import BaseSchema

class OrderCreate(BaseSchema):
    customer_id: int

class OrderStatusUpdate(BaseSchema):
    status: str

class OrderResponse(BaseSchema):
    order_id: int
    customer_id: int

    total_amount: Decimal

    status: str
    payment_method: str
    shipping_address: str