from fastapi import APIRouter,HTTPException
from config.db import db
from schemas.task import studentTaskEntity,studentTasksEntity
from models.task import StudentTask
from bson import ObjectId
from pymongo.errors import PyMongoError

router_task=APIRouter(tags=["Tasks"])

@router_task.post('/api/task', response_model=StudentTask)
async def create_task(task:StudentTask):
    try:
        dict_task = task.dict()
        del dict_task["id"]
        id = db.tasks.insert_one(dict_task).inserted_id
        new_task = db.tasks.find_one({"_id":id})
        new_task = studentTaskEntity(new_task)
        return StudentTask(**new_task)
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router_task.get('/api/task/{id}')
async def get_task(id:str):
    try:
        return studentTaskEntity(db.tasks.find_one({"_id":ObjectId(id)}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router_task.get('/api/tasks/student/{id}')
async def get_student_tasks(id:str):
    try:
        return studentTasksEntity(db.tasks.find({"id_student":(id)}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router_task.put('/api/task/{id}', response_model=StudentTask)
async def put_student_task(id:str, task:StudentTask):
    try:
        edit_task = task.dict()
        del edit_task["id"]
        return studentTaskEntity(db.tasks.find_one_and_update({"_id":ObjectId(id)},{"$set":edit_task}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router_task.delete('/api/task/{id}')
async def delete_student_task(id:str):
    try:
        db.tasks.find_one_and_delete({"_id":ObjectId(id)})
        return {"message":"eliminacion exitosa"}
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))