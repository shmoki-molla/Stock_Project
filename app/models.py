from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv
from sqlalchemy import BigInteger, Date, Time, ForeignKey, String, Boolean, ARRAY
import asyncpg
import psycopg2
import asyncio

load_dotenv()

connection_string = f"postgresql+asyncpg://{os.environ.get("USER")}:{os.environ.get("PASSWORD")}@{os.environ.get("HOST")}:{os.environ.get("PORT")}/{os.environ.get("DB_NAME")}"

engine = create_async_engine(connection_string, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, future=True, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'traders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(20))
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    company: Mapped[list[str]] = mapped_column(ARRAY(String(20)))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
