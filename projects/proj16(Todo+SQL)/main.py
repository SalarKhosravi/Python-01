import time
from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. View Completed Tasks")
        print("4. Complete Task")
        print("5. Remove Task")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            print("\nPending Tasks:")
            manager.list_tasks(completed=0)

        elif choice == "3":
            print("\nCompleted Tasks:")
            manager.list_tasks(completed=1)

        elif choice == "4":
            manager.list_tasks(completed=0)
            task_id = int(input("Enter task ID to complete: "))
            manager.complete_task(task_id)

        elif choice == "5":
            manager.list_tasks(completed=0)
            task_id = int(input("Enter task ID to remove: "))
            manager.remove_task(task_id)

        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            manager.search_tasks(keyword)

        elif choice == "7":
            print("Exiting program...")
            manager.close()
            time.sleep(1)
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
