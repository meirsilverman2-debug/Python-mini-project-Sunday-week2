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

def get_task_service():
    return tasks_mock


def create_task_service(task):

    new_task = {

        "id": len(tasks_mock) + 1,
        "title": task.title,
        "completed": task.completed

    }

    tasks_mock.append(new_task)

    return new_task


def get_task_by_id_service(task_id: int):
    for task in tasks_mock:
        if task["id"] == task_id:
            return task

        return None

    

