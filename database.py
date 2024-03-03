from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
from datetime import date, datetime


engine = create_async_engine(f"")


new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TasksOrm(Model):
    __tablename__ = "tasks"

    close_status: Mapped[bool]
    shift_task_submission: Mapped[str]
    work_center: Mapped[str]
    shift: Mapped[str]
    brigade: Mapped[str]
    partion_number: Mapped[int] = mapped_column(primary_key=True)
    partion_date: Mapped[date]
    nomenclature: Mapped[str]
    ekn_code: Mapped[str]
    rc_id: Mapped[str]
    shift_starts_at: Mapped[datetime]
    shift_ends_at: Mapped[datetime]
    shift_closed: Mapped[datetime | None]


class ProductOrm(DeclarativeBase):
    __tablename__ = "product"

    unique_product_code: Mapped[str]
    partion_number: Mapped[int] = mapped_column(primary_key=True)
    partion_date: Mapped[date]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)