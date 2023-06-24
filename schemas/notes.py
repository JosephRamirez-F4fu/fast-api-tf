def noteEntity(item)->dict:
    return {
        "text":item["text"],
        "title":item["title"]
    }
def studentNoteEntity(item) -> dict:
      
    return {
        "id":str(item["_id"]),
        "id_student": item["id_student"],
        "note": noteEntity(item["note"])
    }

def studentNotesEntity(entity) -> list:
    return [studentNoteEntity(item) for item in entity]