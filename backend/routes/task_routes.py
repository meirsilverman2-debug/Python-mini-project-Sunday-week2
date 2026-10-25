from fastapi import APIRouter, status
from models.task_model import TaskCreate

router = APIRouter()

tasks_mock = [
    {

    "id": 1,
    "title": "Learn Python",
    "completed": False

    },
    {

    "id": 2,
    "title": "Build a REST API",
    "completed": False

    }
]

# GET all tasks:
@router.get("/tasks")
def get_tasks():
    return tasks_mock

# POST creat a new task:
@router.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    
    new_task = {
        "id": len(tasks_mock) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks_mock.append(new_task)

    return new_task
