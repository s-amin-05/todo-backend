from fastapi import APIRouter, Request, Response
from models import Todo
from typing import Annotated


router = APIRouter()

# Create 
@router.post("/", status_code=201)
async def add_todo(todo: Todo, request: Request):
    try:
        request.app.todo_collection.insert_one(todo.model_dump())
        return {"todo": todo}
    except Exception as e:
        print("Insertion error:", e)
        return {"oops": "insertion error"}


# Read
@router.get("/")
async def get_all_todos(request: Request, response: Response):
    try:
        response.set_cookie(key="ayyyy", value="yooo")
        # Removed the _id field because it was giving errors
        todos = []
        cursor = request.app.todo_collection.find({}, {"_id": 0})
        async for todo in cursor:
            todos.append(todo)

        return {"todos": todos}

    except Exception as e:
        print("Read error:", e)
        return {"oops": "read error"}


# Update
@router.patch("/")
async def update_todo(old_todo_title: str, new_todo: Todo, request: Request):
    try:
        query_filter = {"title": old_todo_title}
        update_operation = {'$set':
            new_todo.model_dump()
        }
        request.app.todo_collection.update_one(query_filter, update_operation)
        return {"updated_todo":new_todo}

    except Exception as e:
        print("Update error:", e)
        return {"oops": "update error"}
    

# Delete
@router.delete("/")
async def delete_todo(old_todo_title: str, request: Request):
    try:
        query_filter = {"title": old_todo_title}
        result = request.app.todo_collection.delete_one(query_filter)
        return {"deleted": result.acknowledged}

    except Exception as e:
        print("Delete error:", e)
        return {"oops": "delete error"}
