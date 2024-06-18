import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application

    """

    load_dotenv()

    # App Settings
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI GPT API")
    APP_ENV: str = os.getenv("APP_ENV", "local")
    DEBUG: bool = bool(int(os.getenv("DEBUG", 0)))
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", ["*"]).split(",")

    # MongoDB Settings
    PATH_CERT: str = os.getenv("PATH_CERT")
    MONGO_ENVIRONMENT: str = os.getenv("DATABASE_ENVIRONMENT", "development")
    MONGO_URL: str = os.getenv("MONGO_URL", "mongodb")
    MONGO_SSL: bool = bool(int(os.getenv("MONGO_SSL", 0)))

    # GPT Settings
    GPT_API_KEY: str = os.getenv("GPT_API_KEY")
settings = Settings()