from typing import Optional
from pydantic.main import BaseModel

class Note(BaseModel):
    id: Optional[int]
    title: Optional[str] = None
    data: str
    class Config:
        orm_mode = True