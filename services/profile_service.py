from sqlalchemy.future import select
from models.customer import Customer


class ProfileService:

    @classmethod
    async def get_profile(
        cls,
        db,
        user_id
    ):

        result = await db.execute(
            select(Customer).where(
                Customer.user_id == user_id
            )
        )

        return result.scalar_one_or_none()


    @classmethod
    async def update_profile(
        cls,
        db,
        user_id,
        profile_data
    ):

        result = await db.execute(
            select(Customer).where(
                Customer.user_id == user_id
            )
        )

        customer = result.scalar_one_or_none()

        if not customer:
            return None

        customer.first_name = profile_data.first_name
        customer.last_name = profile_data.last_name
        customer.phone = profile_data.phone
        customer.address = profile_data.address

        await db.commit()
        await db.refresh(customer)

        return customer