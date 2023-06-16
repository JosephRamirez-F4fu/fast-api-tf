from typing import Optional
from pydantic import BaseModel

class SubTask(BaseModel):
    name:str
    isDone:bool

class Task(BaseModel):
    name:str
    isDone:bool
    subtasks:list[SubTask]

class StudentTask(BaseModel):
    id:Optional[str]
    id_student:str
    tasks:Task
