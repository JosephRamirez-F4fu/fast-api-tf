from pydantic import BaseModel
from typing import Optional
class Task(BaseModel):
    id:Optional[str]
    name:str
    description:str
    isDone:bool
