def noteEntity(item)->dict:
    return {
        "text":item["text"],
        "title":item["title"]
    }
def studentNoteEntity(item) -> dict:
    notes = [noteEntity(note) for note in item["notes"]]
    return {
        "id":str(item["_id"]),
        "id_student": item["id_student"],
        "notes": notes
    }

def studentNotesEntity(entity) -> list:
    return [studentNoteEntity(item) for item in entity]