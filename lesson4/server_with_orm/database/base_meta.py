from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_PORT

Base = declarative_base()
engine = create_engine(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}", echo=False)
session_factory = sessionmaker(engine, autocommit=False)


class BaseSQLAlchemyModel(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}