from fastapi import APIRouter
from models import Todo
from database import todo_collection

router = APIRouter()

# Create 
@router.post("/todos/", status_code=201)
async def add_todo(todo: Todo):
    try:
        await todo_collection.insert_one(todo.model_dump())
        return {"todo": todo}
    except Exception as e:
        print("Insertion error:", e)
        return {"oops": "insertion error"}


# Read
@router.get("/todos/")
async def get_all_todos():
    try:
        # Removed the _id field because it was giving errors
        todos = todo_collection.find({}, {"_id": 0})
        todo_list = list(todos)

        return {"todos": todo_list}

    except Exception as e:
        print("Read error:", e)
        return {"oops": "read error"}


# Update
@router.patch("/todos/")
async def update_todo(old_todo_title: str, new_todo: Todo):
    try:
        query_filter = {"title": old_todo_title}
        update_operation = {'$set':
            new_todo.model_dump()
        }
        result = todo_collection.update_one(query_filter, update_operation)
        return {"updated_todo":new_todo}

    except Exception as e:
        print("Update error:", e)
        return {"oops": "update error"}
    

# Delete
@router.delete("/todos/")
async def delete_todo(old_todo_title: str):
    try:
        query_filter = {"title": old_todo_title}
        result = todo_collection.delete_one(query_filter)
        return {"deleted": result.acknowledged}

    except Exception as e:
        print("Delete error:", e)
        return {"oops": "delete error"}
