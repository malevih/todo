from models import ToDo
from services import show_all_tasks

def main():
    t = ToDo(name="Molk")
    print(t)
    print(show_all_tasks)

if __name__ == "__main__":
    main()