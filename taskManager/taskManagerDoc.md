# Task Manager

This script provides a simple task manager implemented in Python. It allows users to add, complete, edit, delete, and view tasks.

## Classes

### TaskManager

This class represents a task manager that maintains an ordered dictionary of tasks.

#### Methods

- `__init__`: Initializes a new instance of the TaskManager class.
- `add_task(task)`: Adds a new task to the task manager.
- `complete_task(task_number)`: Marks a task as completed.
- `edit_task(task_number, new_task)`: Edits the task at the specified index with a new task.
- `delete_task(task_number)`: Deletes the task at the specified index.
- `view_tasks()`: Prints all tasks to the console.
- `save_tasks()`: Saves all tasks to a text file.

## Functions

### main

This function provides a command-line interface for interacting with the TaskManager class. It allows users to add, complete, edit, delete, and view tasks.

## Usage

Run the script in the command line and follow the prompts to manage tasks.

Example of user interface:
python3 taskManager.py

1. Add task
2. Complete task
3. Edit task
4. Delete task
5. View tasks
6. Exit

Enter the number corresponding to the action you want to perform and follow the prompts.