from  services.task_service import (get_task_service, create_task_service, get_task_by_id_service)


def get_tasks_ctrl():
    return get_task_service()


def create_task_ctrl(task):
    return create_task_service(task)


def get_task_by_id_cotrl(task_id: int):
    return get_task_by_id_service(task_id)