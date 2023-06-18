from fastapi import APIRouter,HTTPException
from config.db import db
from schemas.notes import studentNoteEntity,studentNotesEntity
from models.notes import StudentNote
from bson import ObjectId
from pymongo.errors import PyMongoError

router_notes = APIRouter(tags=["Notes"])
notes_collection = db.notes
@router_notes.post('/api/note', response_model=StudentNote)
async def post_note(note:StudentNote):
    try:
        dict_note = note.dict()
        del dict_note["id"]
        id = notes_collection.insert_one(dict_note).inserted_id
        new_note = notes_collection.find_one({"_id":id})
        new_note = studentNoteEntity(new_note)
        return StudentNote(**new_note)
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router_notes.get('/api/note/{id}')
async def get_note(id:str):
    try:
        return studentNoteEntity(notes_collection.find_one({"_id":ObjectId(id)}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))


@router_notes.get('/api/student/notes/{id}')
async def get_student_notes(id:str):
    try:
        return studentNotesEntity(notes_collection.find({"id_student":(id)}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router_notes.put('/api/note/{id}',response_model=StudentNote)
async def put_student_notes(id:str,note:StudentNote):
    try:
        edit_note=note.dict()
        del edit_note["id"]
        return studentNoteEntity(notes_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":edit_note}))
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router_notes.delete('/api/note/{id}')
async def delete_note(id:str):
    try:
        notes=notes_collection.find_one_and_delete({"_id":ObjectId(id)})
        if not notes:
           return {"message":"no se encontro el elemento a eliminar","resultado":False}
        return {"message":"eliminacion exitosa","resultado":True}
    except PyMongoError as e:
        raise HTTPException(status_code=500,detail=str(e))