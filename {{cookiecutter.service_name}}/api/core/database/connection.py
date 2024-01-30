from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from api.core.settings import settings


def engine_create(*args, **kwargs):
    return create_engine(settings.db.SQLALCHEMY_DATABASE_URL, *args, **kwargs)


def get_session():
    with Session(engine) as session:
        yield session


engine = engine_create()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
