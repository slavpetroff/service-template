from typing import Any, Optional

from pydantic import BaseModel, Field


class CommonDatabaseSettings(BaseModel):
    """
    Base class for database settings.
    """

    database_protocol: str = "sqlite"
    database_name: str = "app.db"

    # Add more fields which are used in postgres
    database_username: Optional[str] = None
    database_password: Optional[str] = Field(
        default_factory=lambda: None, alias="password"
    )
    database_host: Optional[str] = None
    database_port: Optional[int] = None

    SQLALCHEMY_DATABASE_URL: str = None

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.SQLALCHEMY_DATABASE_URL = self.get_database_url()

    def get_database_url(self):
        match self.database_protocol:
            case "sqlite":
                return f"{self.database_protocol}:///./{self.database_name}"
            case "postgresql":
                return (
                    f"{self.database_protocol}://{self.database_username}"
                    f":{self.database_password}@{self.database_host}"
                    f":{self.database_port}/{self.database_name}"
                )
            case _:
                raise ValueError(f"Invalid database protocol: {self.database_protocol}")


class LocalDatabaseSettings(CommonDatabaseSettings):
    """
    Local database settings.
    """

    database_name: str = "local.db"
    database_protocol: str = "sqlite"


class TestDatabaseSettings(CommonDatabaseSettings):
    """
    Test database settings.
    """

    database_name: str = ":memory:"
    database_protocol: str = "sqlite"

    def get_database_url(self):
        return f"{self.database_protocol}:///{self.database_name}"


class DevDatabaseSettings(CommonDatabaseSettings):
    """
    Development database settings.
    """

    database_name: str = "postgres"
    database_protocol: str = "postgresql"
    database_port: int = 5432
    database_host: str = "192.168.1.100"
    database_username: str = "admin"
    database_password: str = "admin"


class ProductionDatabaseSettings(CommonDatabaseSettings):
    """
    Production database settings.
    """

    database_name: str = "prod"
    database_protocol: str = "postgresql"
    database_port: int = 5432
    database_host: str = "192.168.1.200"
    database_username: str = "admin"
    database_password: str = "admin"
