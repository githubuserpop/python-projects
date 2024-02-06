import sys
from collections import OrderedDict
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = OrderedDict()

    def add_task(self, task):
        self.tasks[task] = {"status": False, "updates": [f"Added on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]}
        self.view_tasks()
        self.save_tasks()

    def complete_task(self, task_number):
        task = list(self.tasks.keys())[task_number - 1]
        self.tasks[task]["status"] = True
        self.tasks[task]["updates"].append(f"Completed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.view_tasks()
        self.save_tasks()

    def edit_task(self, task_number, new_task):
        task = list(self.tasks.keys())[task_number - 1]
        updates = self.tasks[task]["updates"]
        self.tasks[new_task] = {"status": self.tasks[task]["status"], "updates": updates}
        self.tasks[new_task]["updates"].append(f"Edited on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        del self.tasks[task]
        self.view_tasks()
        self.save_tasks()

    def delete_task(self, task_number):
        task = list(self.tasks.keys())[task_number - 1]
        self.tasks[task]["updates"].append(f"Deleted on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.save_tasks()
        del self.tasks[task]
        self.view_tasks()

    def view_tasks(self):
        print("\n" + "-" * 50)
        for i, (task, info) in enumerate(self.tasks.items(), start=1):
            print(f"{i}. Task: {task}, Completed: {info['status']}")
        print("-" * 50 + "\n")

    def save_tasks(self):
        with open('tasks.txt', 'w') as f:
            for task, info in self.tasks.items():
                f.write(f"Task: {task}, Completed: {info['status']}\n")
                for update in info["updates"]:
                    f.write(f"  {update}\n")

def main():
    task_manager = TaskManager()
    while True:
        print("\n" + "=" * 50)
        print("1. Add task")
        print("2. Complete task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. View tasks")
        print("6. Exit")
        print("=" * 50 + "\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter task number to complete: "))
            task_manager.complete_task(task_number)
        elif choice == '3':
            task_number = int(input("Enter task number to edit: "))
            new_task = input("Enter new task: ")
            task_manager.edit_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            task_manager.delete_task(task_number)
        elif choice == '5':
            task_manager.view_tasks()
        elif choice == '6':
            sys.exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()