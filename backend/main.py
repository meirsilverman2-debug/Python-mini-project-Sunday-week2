from fastapi import FastAPI
from routes.task_routes import router as task_router
from core.logger import logger

app = FastAPI()

@app.get("/")
def home():
    logger.info("Home endpoint was called")
    return {"message": "Hello from Python!"}

app.include_router(task_router)