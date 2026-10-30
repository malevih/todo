from models import Task
class TaskService:
    def __init__(self):
        self._tasks: list[Task] = []
        self._task_id = 1

    def add_task(self, name: str, description: str | None = None) -> Task:
        task = Task(name, self._task_id, description)
        self._tasks.append(task)
        self._task_id += 1
        return task


    def get_all_tasks(self):
        return tuple(self._tasks)