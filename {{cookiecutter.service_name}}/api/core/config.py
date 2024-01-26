from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.project_name}}"
    admin_email: str


settings = Settings()
