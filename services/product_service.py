from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import *
from schemas import *
from schemas.product import ProductCreate, ProductUpdate

from sqlalchemy import or_


class ProductService:
    @staticmethod
    async def list_products(db: AsyncSession):
        result = await db.execute(select(Product))
        return result.scalars().all()
    @staticmethod
    async def create_product(db: AsyncSession, data:ProductCreate):
        new_prod = Product(**data.model_dump())
        db.add(new_prod)
        await db.commit()
        await db.refresh(new_prod)
        return new_prod

    @staticmethod
    async def delete_product(
            db: AsyncSession,
            prod_id: int
    ):

        result = await db.execute(
            select(Product).where(
                Product.product_id == prod_id
            )
        )

        product = result.scalar_one_or_none()

        if not product:
            return None

        cart_check = await db.execute(
            select(CartItem).where(
                CartItem.product_id == prod_id
            )
        )

        if cart_check.scalar_one_or_none():
            raise HTTPException(
                status_code=400,
                detail="Cannot delete product because it exists in cart"
            )

        try:
            await db.delete(product)
            await db.commit()
            return True

        except IntegrityError:
            await db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Cannot delete product because it exists in orders"
            )
    @staticmethod
    async def update_product(db: AsyncSession, prod_id:int, data:ProductUpdate):
        result = await db.execute(select(Product).where(Product.product_id == prod_id))
        db_prod = result.scalar_one_or_none()
        if not db_prod:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(db_prod, key, value)

        await db.commit()
        await db.refresh(db_prod)
        return db_prod

    @staticmethod
    async def get_product(
            db: AsyncSession,
            product_id: int
    ):
        result = await db.execute(
            select(Product)
            .where(Product.product_id == product_id)
        )

        return result.scalar_one_or_none()


    @staticmethod
    async def search_products(
            db: AsyncSession,
            query: str
    ):
        result = await db.execute(
            select(Product)
            .where(
                or_(
                    Product.name.ilike(f"%{query}%"),
                    Product.brand.ilike(f"%{query}%")
                )
            )
        )

        return result.scalars().all()
