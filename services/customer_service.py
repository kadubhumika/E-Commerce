from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Customer
from schemas.customer import CustomerUpdate


class CustomerService:
    @staticmethod
    async def get_profile(db: AsyncSession, customer_id: int):
        result = await db.execute(select(Customer).where(Customer.customer_id == customer_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_profile(db: AsyncSession, customer_id: int, data: CustomerUpdate):
        result = await db.execute(select(Customer).where(Customer.customer_id == customer_id))
        customer = result.scalar_one_or_none()
        if not customer:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(customer, key, value)

        await db.commit()
        await db.refresh(customer)
        return customer
