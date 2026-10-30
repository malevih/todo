from models import ToDo
task_id = 1

tasks = []

def add_task(tasks, task:ToDo):
    tasks.appent(task)
    task_id += 1
    return task


def show_all_tasks():
    return tuple(tasks)