from uuid import UUID
from typing import Union
from pydantic import BaseModel

class Book(BaseModel):
    id: Union[int, str, UUID]
    title: str
    author: str
    description: str

