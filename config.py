from typing import Set
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Notes"
    APP_VERSION: str = "0.0.1"
    POSTGRES_URI: str = "postgres://guest:guest@localhost:5432/notesdb"
    
settings = Settings()