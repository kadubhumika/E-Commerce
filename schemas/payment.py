from decimal import Decimal
from schemas.base import BaseSchema

class PaymentCreate(BaseSchema):
    order_id: int
    amount: Decimal
    payment_method: str

class PaymentUpdate(BaseSchema):
    payment_method: str | None = None

class PaymentResponse(BaseSchema):
    payment_id: int
    order_id: int
    amount: Decimal
    status: str