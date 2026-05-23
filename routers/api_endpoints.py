from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from core.db import get_db
from schemas.auth import *
from schemas.category import CategoryResponse, CategoryCreate
from schemas.order import *

from schemas.product import *

from schemas.cart_item import *


from services.auth_service import AuthService
from services.category_service import CategoryService
from services.product_service import ProductService
from services.cart_service import CartService
from services.order_service import OrderService

router = APIRouter()


@router.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister, db: AsyncSession = Depends(get_db)):
    created = await AuthService.register_user(db, user)
    if not created:
        raise HTTPException(status_code=400, detail="Email already registered")
    return created

@router.post("/auth/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    valid_user = await AuthService.login_user(db, credentials)
    if not valid_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": f"mocked-jwt-token-for-user-{valid_user.id}", "token_type": "bearer"}

# --- PRODUCT ENDPOINTS ---
@router.get("/products", response_model=List[ProductResponse])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    return await ProductService.list_products(db)

@router.post("/products", response_model=ProductResponse)
async def add_new_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await ProductService.create_product(db, product)

# --- CART ENDPOINTS ---
@router.post("/cart/items", response_model=CartItemResponse)
async def add_item_to_basket(item: CartItemCreate, db: AsyncSession = Depends(get_db)):
    added = await CartService.add_item_to_cart(db, item)
    if not added:
        raise HTTPException(status_code=400, detail="Could not add item. Out of stock or invalid data.")
    return added

# --- CHECKOUT ENDPOINTS ---
@router.post("/orders/checkout/{customer_id}", response_model=OrderResponse)
async def process_checkout(customer_id: int, payment_method: str, db: AsyncSession = Depends(get_db)):
    placed_order = await OrderService.checkout_cart(db, customer_id, payment_method)
    if not placed_order:
        raise HTTPException(status_code=400, detail="Checkout failed. Cart is empty or invalid details.")
    return placed_order
# --- CATEGORY ENDPOINTS ---
@router.get("/categories", response_model=List[CategoryResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await CategoryService.list_categories(db)

@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def add_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await CategoryService.create_category(db, category)
    except Exception:
        # Prevents 500 error if someone inserts a duplicate category name
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category name already exists or data is invalid."
        )
