from sqlmodel import create_engine, SQLModel
from app.core.settings import POSTGRESQL_URI

engine = create_engine(POSTGRESQL_URI)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
