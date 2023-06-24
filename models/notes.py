from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    title:str
    text:str

class StudentNote(BaseModel):
    id:Optional[str]
    id_student:str
    note:Note
