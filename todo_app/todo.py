import json
import os
import sys

class Task:
    """Class representing an individual to-do task."""
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} Title: {self.title} | Category: {self.category}\n    Description: {self.description}"

# Path to local storage file
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

def save_tasks(tasks, filename=TASKS_FILE):
    """Save all tasks to a JSON file."""
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(filename=TASKS_FILE):
    """Load tasks from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_task(tasks):
    """Prompt user to add a new task."""
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    description = input("Enter task description: ").strip()
    category = input("Enter category (e.g., Work, Personal, Urgent): ").strip()
    if not category:
        category = "General"
    
    task = Task(title, description, category)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Success: Task '{title}' added successfully!")

def view_tasks(tasks):
    """Display all tasks with status and details."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks found. Add a task to get started!")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "[Completed]" if task.completed else "[Pending]"
        print(f"{idx}. {status} [{task.category}] {task.title}")
        print(f"   Description: {task.description}")

def edit_task(tasks):
    """Edit an existing task's title, description, or category."""
    print("\n--- Edit Task ---")
    if not tasks:
        print("No tasks available to edit.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to edit: "))
        if 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            print(f"\nEditing Task #{choice}: '{task.title}' (Press Enter to keep current value)")
            
            new_title = input(f"New title [{task.title}]: ").strip()
            new_desc = input(f"New description [{task.description}]: ").strip()
            new_cat = input(f"New category [{task.category}]: ").strip()

            if new_title:
                task.title = new_title
            if new_desc:
                task.description = new_desc
            if new_cat:
                task.category = new_cat

            save_tasks(tasks)
            print(f"Success: Task #{choice} updated successfully!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def mark_task_completed(tasks):
    """Mark a task as completed by index."""
    print("\n--- Mark Task Completed ---")
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1].mark_completed()
            save_tasks(tasks)
            print(f"Success: Task '{tasks[choice - 1].title}' marked as completed!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task(tasks):
    """Delete a task by index."""
    print("\n--- Delete Task ---")
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            deleted = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Success: Task '{deleted.title}' deleted successfully!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    """Main command-line interface loop."""
    tasks = load_tasks()
    while True:
        print("\n==========================================")
        print("      Personal To-Do List Application     ")
        print("==========================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Thank you for using Personal To-Do List Application!")
            break
        else:
            print("Error: Invalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
