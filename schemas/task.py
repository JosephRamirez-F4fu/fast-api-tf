def taskEntity(item)->dict:
    return {
        "id": str(item["_id"]),
        "name":item["name"],
        "description":item["description"],
        "isDone":item["isDone"]
    }

def tasksEntity(entity)->list:
    return [taskEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}
            
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]