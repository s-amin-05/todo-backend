from models import Todo
from fastapi import FastAPI
from routes import router
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
app.include_router(router)

