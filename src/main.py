from models import Todo
from fastapi import FastAPI
from routes import router
from dotenv import load_dotenv
from database import connect_db

load_dotenv()


app = FastAPI(title="TodoList", description="This is a basic CRUD app for todos", lifespan=connect_db)

app.include_router(router, prefix='/todos')



