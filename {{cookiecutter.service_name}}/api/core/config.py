from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Microservice"
    admin_email: str


settings = Settings()
