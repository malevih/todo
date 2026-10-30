from models import Task
from service import TaskService

def main():
    todo_service = TaskService()
    t = Task(id = 1, name="buy Milk", description="1,5l")
    print(t)
    todo_service.add_task("Vodka")
    todo_service.add_task("PYTHON", "make python homework")
    for t in todo_service.get_all_tasks():
        print(t);

if __name__ == "__main__":
    main()