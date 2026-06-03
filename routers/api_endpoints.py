from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core.dependencies import get_current_user

from core.db import get_db

from fastapi.security import OAuth2PasswordRequestForm
from core.security import create_access_token
from schemas.profile import *
from services.profile_service import ProfileService
from models import AuthUser

# Schemas
from schemas.auth import *
from schemas.category import CategoryCreate, CategoryResponse
from schemas.product import *
from schemas.cart_item import *
from schemas.order import *
from schemas.review import ReviewCreate, ReviewResponse
from core.role_dependencies import (
    admin_required,
    customer_required
)

# Services
from services.auth_service import AuthService
from services.category_service import CategoryService
from services.product_service import ProductService
from services.cart_service import CartService
from services.order_service import OrderService
from services.review_service import ReviewService

router = APIRouter()


# ====================================================
# 1. AUTH
# ====================================================

@router.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    created = await AuthService.register_user(db, user)

    if not created:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return created




@router.post(
    "/auth/login",
    response_model=TokenResponse
)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_db)
):
    login_data = UserLogin(
        email=form_data.username,
        password=form_data.password
    )

    valid_user = await AuthService.login_user(
        db,
        login_data
    )

    if not valid_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(valid_user.id),
            "role": valid_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ====================================================
# 2. CATEGORY
# ====================================================

@router.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
async def add_category(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(admin_required)
):
    try:
        return await CategoryService.create_category(
            db,
            category
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )


@router.get(
    "/categories",
    response_model=List[CategoryResponse]
)
async def get_categories(
    db: AsyncSession = Depends(get_db)

):
    return await CategoryService.list_categories(db)


# ====================================================
# 3. PRODUCTS
# ====================================================

@router.post(
    "/products",
    response_model=ProductResponse
)
async def add_new_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(admin_required)

):
    return await ProductService.create_product(
        db,
        product
    )


@router.get(
    "/products",
    response_model=List[ProductResponse]
)
async def get_all_products(
    db: AsyncSession = Depends(get_db)
):
    return await ProductService.list_products(db)


@router.put(
    "/products/{prod_id}",
    response_model=ProductResponse
)
async def update_product(
    prod_id: int,
    product: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(admin_required)

):
    updated = await ProductService.update_product(
        db,
        prod_id,
        product
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated


@router.delete("/products/{prod_id}")
async def delete_product(
    prod_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(admin_required)

):
    deleted = await ProductService.delete_product(
        db,
        prod_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Deleted successfully"
    }


# ====================================================
# 4. CART
# ====================================================

@router.post(
    "/cart/items",
    response_model=CartItemResponse
)
async def add_item_to_basket(
    item: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    added = await CartService.add_item_to_cart(
        db,
        item
    )

    if not added:
        raise HTTPException(
            status_code=400,
            detail="Could not add item"
        )

    return added


@router.get(
    "/cart/{cart_id}",
    response_model=List[CartItemResponse]
)
async def view_cart(
    cart_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    return await CartService.view_cart_items(
        db,
        cart_id
    )


@router.delete("/cart/items/{cart_item_id}")
async def delete_cart_item(
    cart_item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    deleted = await CartService.remove_item(
        db,
        cart_item_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {
        "message": "Deleted"
    }


# ====================================================
# 5. ORDERS
# ====================================================

@router.put(
    "/orders/{order_id}/status",
    response_model=OrderResponse
)
async def update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(admin_required)
):

    updated = await OrderService.update_order_status(
        db,
        order_id,
        data.status
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return updated

@router.post(
    "/orders/checkout/{customer_id}",
    response_model=OrderResponse
)
async def process_checkout(
    customer_id: int,
    payment_method: str,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    placed_order = await OrderService.checkout_cart(
        db,
        customer_id,
        payment_method
    )

    if not placed_order:
        raise HTTPException(
            status_code=400,
            detail="Checkout failed"
        )

    return placed_order
@router.get(
    "/orders/my-orders",
    response_model=List[OrderResponse]
)
async def my_orders(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):

    customer = await ProfileService.get_customer_by_user_id(
        db,
        current_user.id
    )

    return await OrderService.get_orders(
        db,
        customer.customer_id
    )


# ====================================================
# 6. REVIEWS
# ====================================================

@router.post(
    "/reviews",
    response_model=ReviewResponse
)
async def add_review(
    review: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    created = await ReviewService.add_review(
        db,
        review
    )

    if not created:
        raise HTTPException(
            status_code=400,
            detail="Already reviewed"
        )

    return created


@router.get(
    "/reviews/{product_id}",
    response_model=List[ReviewResponse]
)
async def get_reviews(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):
    return await ReviewService.get_reviews(
        db,
        product_id
    )
# ====================================================
# PROFILE
# ====================================================

@router.get(
    "/profile",
    response_model=ProfileResponse
)
async def get_profile(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):

    return await ProfileService.get_profile(
        db,
        current_user.id
    )


@router.put(
    "/profile",
    response_model=ProfileResponse
)
async def update_profile(
    profile: ProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(customer_required)
):

    updated = await ProfileService.update_profile(
        db,
        current_user.id,
        profile
    )

    return updated


# ====================================================
# 7. HOME
# ====================================================

@router.get("/")
async def home():
    return {
        "message":
        "E-Commerce API running successfully"
    }