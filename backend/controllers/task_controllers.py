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

def get_tasks_ctrl():
    return tasks_mock


def create_task_ctrl(task):

    new_task = {
        "id": len(tasks_mock) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks_mock.append(new_task)

    return new_task