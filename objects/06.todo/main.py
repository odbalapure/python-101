from todo_list import TodoList
from task import Task

def main() -> None:
    print("*" * 98)
    print("\t\t\t\t\tTo-Do Application")
    print("*" * 98)
    td = TodoList()

    task1 = Task(1, "Pay bills")
    task2 = Task(2, "Buy shoes")
    task3 = Task(3, "Send a parcel")
    task4 = Task(4, "Read a book")

    td.add_task(task1)
    td.add_task(task2)
    td.add_task(task3)
    td.add_task(task4)
    
    print("\n\n................. Added tasks in list .................")
    for task in td.tasks:
        print(task)

    td.delete_task(2)
    print("................. Updated list: After a task deletion .................")
    for task in td.tasks:
        print(task)

    td.edit_task_description(1, "Complete project")
    print("................. Updated list: After editing a task description .................")
    for task in td.tasks:
        print(task)

    td.edit_task_state(1, "completed")
    print("................. Updated list: After editing a task state .................")
    for task in td.tasks:
        print(task)

if __name__ == "__main__":
    main()