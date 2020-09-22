from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Notes"
    APP_VERSION: str = "0.0.2"
    POSTGRESQL_HOSTNAME: str = "localhost"
    POSTGRESQL_USERNAME: str = "guest"
    POSTGRESQL_PASSWORD: str = "guest"
    POSTGRESQL_DATABASE: str = "notesdb"


settings = Settings()
