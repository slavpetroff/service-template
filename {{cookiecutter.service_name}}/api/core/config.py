from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.service_name}}"
    admin_email: str


settings = Settings()
