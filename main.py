from fastapi import FastAPI

from routers.api_endpoints import router
# Import all your models here so SQLAlchemy registers them at runtime
from models.auth_user import AuthUser
from models.customer import Customer
from models.product import Product
from models.cart import Cart
from models.order import Order
from models.review import Review


app = FastAPI()


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Ecommerce Backend Running"
    }