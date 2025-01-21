from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import asyncio

DB_NAME="todolist"
uri = os.getenv("MONGODB_URI")

def connect_db():
    try:
        mongo_client = MongoClient(uri)
        mongo_client.admin.command("ping")

        database = mongo_client["Cluster0"]

        if "todos" not in database.list_collection_names():
            collection = database.create_collection("todos")

        else:
            collection = database["todos"]

        print(collection)
        return collection
          

    except Exception as e:
        print(f"MongoDB Connection Error: {e}")
        return None

todo_collection = connect_db()