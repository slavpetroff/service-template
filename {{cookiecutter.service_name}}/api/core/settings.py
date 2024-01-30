import os

from pydantic_settings import BaseSettings
from api.core.database.config import (
    DevDatabaseSettings,
    LocalDatabaseSettings,
    ProductionDatabaseSettings,
    TestDatabaseSettings,
)

# Determine the environment from an environment variable
ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV").upper()


class CommonSettings(BaseSettings):
    """
    Example of a main settings file.
    """

    username: str = "username"
    password: str = "password"


class TestSettings(CommonSettings):
    """
    Test settings.
    """

    username: str = "test"
    password: str = "test"

    db: TestDatabaseSettings = TestDatabaseSettings()


class LocalSettings(CommonSettings):
    """
    Local settings.
    """

    username: str = "local"
    password: str = "local"

    db: LocalDatabaseSettings = LocalDatabaseSettings()


class DevSettings(CommonSettings):
    """
    Development settings.
    """

    username: str = "dev"
    password: str = "dev"

    db: DevDatabaseSettings = DevDatabaseSettings()


class ProductionSettings(CommonSettings):
    """
    Production settings.
    """

    username: str = "prod"
    password: str = "prod"

    db: ProductionDatabaseSettings = ProductionDatabaseSettings()


# This is the object containing all our settings
# Do not import the classes above, but this object
match ENVIRONMENT:
    case "LOCAL":
        settings = LocalSettings()
    case "TEST":
        settings = TestSettings()
    case "DEV":
        settings = DevSettings()
    case "PRODUCTION":
        settings = ProductionSettings()
    case _:
        raise ValueError(f"Invalid environment: {ENVIRONMENT}")
