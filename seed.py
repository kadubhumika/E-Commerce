# seed.py

import asyncio
from decimal import Decimal

from core.db import SessionLocal

from models import (
    Category,
    Product,
    AuthUser,
    Customer,
    Cart
)

from security.password_handler import hash_password


async def seed():

    async with SessionLocal() as db:

        # -----------------
        # Categories
        # -----------------

        categories = [
            Category(name="Electronics"),
            Category(name="Laptops"),
            Category(name="Smartphones"),
            Category(name="Books"),
            Category(name="Fashion"),
            Category(name="Gaming"),
            Category(name="Accessories"),
            Category(name="Home Appliances")
        ]

        db.add_all(categories)
        await db.commit()

        # -----------------
        # Users
        # -----------------

        admin = AuthUser(
            email="admin@test.com",
            password_hash=hash_password("admin123"),
            role="admin"
        )

        customer_user = AuthUser(
            email="customer@test.com",
            password_hash=hash_password("customer123"),
            role="customer"
        )

        db.add_all([admin, customer_user])
        await db.commit()

        await db.refresh(admin)
        await db.refresh(customer_user)

        # -----------------
        # Customers
        # -----------------

        admin_customer = Customer(
            user_id=admin.id,
            username="admin",
            first_name="Admin",
            last_name="User",
            phone="9999999999",
            address="Mumbai",
            city="Mumbai",
            state="Maharashtra",
            country="India",
            pincode="400001"
        )

        john = Customer(
            user_id=customer_user.id,
            username="john",
            first_name="John",
            last_name="Doe",
            phone="8888888888",
            address="Pune",
            city="Pune",
            state="Maharashtra",
            country="India",
            pincode="411001"
        )

        db.add_all([admin_customer, john])
        await db.commit()

        await db.refresh(admin_customer)
        await db.refresh(john)

        # -----------------
        # Carts
        # -----------------

        cart1 = Cart(customer_id=admin_customer.customer_id)
        cart2 = Cart(customer_id=john.customer_id)

        db.add_all([cart1, cart2])
        await db.commit()

        # -----------------
        # Products
        # -----------------

        products = [

            Product(
                name="iPhone 15",
                description="Apple smartphone",
                price=Decimal("79999"),
                stock_quantity=20,
                image_url="iphone.jpg",
                category_id=1,
                brand="Apple",
                rating=Decimal("4.8"),
                discount=10
            ),

            Product(
                name="Samsung S25",
                description="Samsung flagship",
                price=Decimal("74999"),
                stock_quantity=15,
                image_url="s25.jpg",
                category_id=1,
                brand="Samsung",
                rating=Decimal("4.7"),
                discount=8
            ),

            Product(
                name="MacBook Air M4",
                description="Apple laptop",
                price=Decimal("129999"),
                stock_quantity=10,
                image_url="macbook.jpg",
                category_id=2,
                brand="Apple",
                rating=Decimal("4.9"),
                discount=5
            ),

            Product(
                name="PS5",
                description="Gaming Console",
                price=Decimal("54999"),
                stock_quantity=12,
                image_url="ps5.jpg",
                category_id=6,
                brand="Sony",
                rating=Decimal("4.8"),
                discount=12
            ),

            Product(
                name="Atomic Habits",
                description="Book",
                price=Decimal("499"),
                stock_quantity=100,
                image_url="atomic.jpg",
                category_id=4,
                brand="Penguin",
                rating=Decimal("4.9"),
                discount=0
            ),
        ]

        db.add_all(products)
        await db.commit()

        print("Database seeded successfully")


if __name__ == "__main__":
    asyncio.run(seed())