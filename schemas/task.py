def subtaskEntity(item) -> dict:
    return {
        "name": item["name"],
        "isDone": item["isDone"]
    }


def taskEntity(item) -> dict:
    subtasks = [subtaskEntity(subtask) for subtask in item["subtasks"]]
    return {
        "name": item["name"],
        "isDone": item["isDone"],
        "subtasks": subtasks
    }


def studentTaskEntity(item) -> dict:
    tasks = taskEntity(item["tasks"])
    return {
        "id":str(item["_id"]),
        "id_student": str(item["id_student"]),
        "tasks": tasks
    }

def studentTasksEntity(entity) -> list:
    return [studentTaskEntity(item) for item in entity]

def tasksEntity(entity) -> list:
    return [taskEntity(item) for item in entity]

def subtasksEntity(entity) -> list:
    return [subtaskEntity(item) for item in entity]
