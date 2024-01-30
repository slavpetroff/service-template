"""
This file contains the fixtures for the tests.
"""

import pytest
from starlette.testclient import TestClient

from api.core.database.connection import SessionLocal, engine_create, get_session
from api.main import app
from api.models import Base


@pytest.fixture(scope="session")
def engine():
    """
    Engine fixture to be used in every session.

    :return: Engine
    """

    engine = engine_create(echo=False, connect_args={"check_same_thread": False})
    return engine


@pytest.fixture(scope="session")
def session(engine):
    """
    Session fixture to be used in every session.

    It generates the tables and drops them after every test run.

    :param engine: Engine to be used
    :return: Session
    """

    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    # Create all the tables
    Base.metadata.create_all(bind=engine)

    yield session

    # Drop all the tables
    Base.metadata.drop_all(bind=engine)

    transaction.rollback()
    session.close()
    connection.close()


@pytest.fixture
def client(session):
    """
    Test client fixture to be used in every test.

    Overrides the get_session dependency to use our session fixture,
    instead of the default one.
    That way, we can use in-memory SQLite for our tests.

    :param session: Session to be used
    :return: TestClient
    """

    def override_get_session():
        return session

    app.dependency_overrides[get_session] = override_get_session  # type: ignore
    yield TestClient(app)
    del app.dependency_overrides[get_session]  # type: ignore
