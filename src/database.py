from fastapi import FastAPI, APIRouter
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
import os
from contextlib import asynccontextmanager
from models import Todo

DB_NAME="todolist"
uri = os.getenv("MONGODB_URI")


@asynccontextmanager
async def connect_db(app: FastAPI):
    
    try:
        mongo_client = AsyncIOMotorClient(uri)
        mongo_client.admin.command("ping")

        database = mongo_client["Cluster0"]

        pong = await database.command("ping")
        if int(pong["ok"]) != 1:
            raise Exception("Cluster connection is not okay!")

        collection_names = await database.list_collection_names()
        if "todos" not in collection_names:
            app.todo_collection = await database.create_collection("todos")

        else:
            app.todo_collection = database.get_collection("todos")

        print(app.todo_collection.name)
        

    except Exception as e:
        print(f"MongoDB Connection Error: {e}")

    finally:
        yield

        mongo_client.close()
        
