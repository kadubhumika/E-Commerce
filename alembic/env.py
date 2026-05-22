import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
# 🔴 CHANGED: Import the async version of the engine config loader
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# 1. Import your Base configuration
from models.base import Base

# 2. Crucial Step: Import ALL your models here so Alembic indexes them!
from models.auth_user import AuthUser
from models.customer import Customer
from models.category import Category
from models.product import Product
# 🔴 ADDED: Make sure your missing models are also imported here!
from models.cart import *
from models.order import *
from models.review import *
from models.customer import *


# This is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata to look for structural changes
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Helper method to run actual structural updates inside the async context stream."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using an Asynchronous Engine."""
    # 🔴 CHANGED: Uses async_engine_from_config to prevent driver mismatch crashes
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # Transfer control smoothly to the synchronous-style migrator tool stream
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    # 🔴 CHANGED: Bootstraps the async runtime loops since Alembic runs synchronously by default
    asyncio.run(run_migrations_online())
