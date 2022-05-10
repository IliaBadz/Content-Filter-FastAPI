import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str = os.getenv("API_KEY")


settings = Settings()
