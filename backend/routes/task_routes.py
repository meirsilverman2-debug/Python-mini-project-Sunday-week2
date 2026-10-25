from fastapi import APIRouter, status
from models.task_model import TaskCreate
from controllers.task_controllers import get_tasks_ctrl, create_task_ctrl

router = APIRouter()



# GET all tasks:
@router.get("/tasks")
def get_tasks_route():
    return get_tasks_ctrl()


# POST creat a new task:
@router.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task_route(task: TaskCreate):
    return create_task_ctrl(task)
