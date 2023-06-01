from fastapi import APIRouter, Response, status,HTTPException
from config.db import db
from schemas.task import taskEntity,tasksEntity
from models.task import Task
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT,HTTP_205_RESET_CONTENT

router_task=APIRouter()

@router_task.get('/tasks')
async def find_all_tasks():
    return tasksEntity(db.task.find())

@router_task.get('/tasks/{id}')
async def find_one_task(id:str):
    return taskEntity(db.task.find_one({"_id":ObjectId(id)}))

@router_task.post('/tasks',response_model=Task,status_code=status.HTTP_201_CREATED)
async def create_task(task:Task):
    new_task = dict(task)
    del new_task["id"]
    id = db.task.insert_one(new_task).inserted_id
    task = db.task.find_one({"_id":id})
    task = taskEntity(task)
    return Task(**task) 

@router_task.put('/tasks/{id}')
async def update_task(id:str,task:Task):
    db.task.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(task)})
    return Response(status_code=HTTP_205_RESET_CONTENT)

@router_task.delete('/tasks/{id}')
async def delete_tasks():
    taskEntity(db.task.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
