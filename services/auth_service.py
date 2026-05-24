from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from models import *
from models.cart import Cart
from schemas.auth import *
from passlib.context import CryptContext

from security.password_handler import pwd_context


class AuthService:


    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    )

    def hash_password(password):
        return pwd_context.hash(password)

    def verify_password(
            plain_password,
            hashed_password
    ):
        return pwd_context.verify(
            plain_password,
            hashed_password
        )
    @classmethod
    async def register_user(cls,db:AsyncSession, user_data:UserRegister):
        existing_user = await db.execute(select(AuthUser).where(AuthUser.email == user_data.email))
        if existing_user.scalar_one_or_none():
            return None
        new_auth = AuthUser(
            email = user_data.email,
            password_hash= cls.hash_password(user_data.password)
        )
        db.add(new_auth)
        await db.flush()
        new_customer = Customer(
            user_id=new_auth.id,
            username=user_data.username,
            first_name="",
            last_name="",
            phone="",
            address=""
        )
        db.add(new_customer)
        await db.flush()
        new_cart = Cart(customer_id=new_customer.customer_id)
        db.add(new_cart)

        await db.commit()
        return new_auth
    @classmethod
    async def login_user(cls,db:AsyncSession, login_data:UserLogin):
        result = await db.execute(
            select(AuthUser).where(
                AuthUser.email ==
                login_data.email
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            return None

        if not cls.verify_password(
                login_data.password,
                user.password_hash
        ):
            return None

        return user