from fastapi import FastAPI
from routes.task_routes import router as task_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Python!"}

app.include_router(task_router)