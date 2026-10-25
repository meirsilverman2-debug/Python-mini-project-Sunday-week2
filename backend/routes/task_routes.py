from fastapi import APIRouter, status, HTTPException
from models.task_model import TaskCreate, TaskUpdate
from controllers.task_controllers import get_tasks_ctrl, create_task_ctrl, get_task_by_id_cotrl, update_task_ctrl

router = APIRouter()


# GET all tasks:
@router.get("/tasks")
def get_tasks_route():
    return get_tasks_ctrl()


# POST creat a new task:
@router.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task_route(task: TaskCreate):
    return create_task_ctrl(task)


# GET one task by id:
@router.get("/tasks/{task_id}")
def get_task_by_id_route(task_id: int):
    task =  get_task_by_id_cotrl(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"

        )

    return task


# PUT/PATCH a task meaning update:
@router.patch("/tasks/{task_id}")
def update_task_route(task_id: int, task_data: TaskUpdate):

    updated_task = update_task_ctrl(task_id, task_data.model_dump(exclude_unset=True))

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            details="Task not found",
        )

    return updated_task
