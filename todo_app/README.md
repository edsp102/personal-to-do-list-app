# Personal To-Do List Application

A lightweight, feature-rich **Personal To-Do List Application** written in Python. This application allows users to create, view, edit, mark as completed, and delete tasks with full data persistence using a local JSON file (`tasks.json`).

---

## Table of Contents
1. [Project Objective](#project-objective)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Environment & Requirements](#environment--requirements)
5. [How to Run the Application](#how-to-run-the-application)
6. [Command-Line Interface (CLI) Guide](#command-line-interface-cli-guide)
7. [Testing & Verification](#testing--verification)

---

## Project Objective
Develop a **Personal To-Do List Application** that emphasizes user interaction and local file handling without requiring external database setups or complex deployment.

---

## Features
- **Task Management**:
  - **Create**: Add new tasks with title, description, and custom category.
  - **View**: Display all tasks with `[Completed]` or `[Pending]` status indicators.
  - **Edit**: Modify title, description, or category of existing tasks.
  - **Mark Completed**: Toggle completion status for any task.
  - **Delete**: Remove tasks from the list by task number.
- **Categorization**: Group tasks by categories such as `Work`, `Personal`, `Urgent`, or custom categories.
- **Persistence**: Automatically save and load tasks from `tasks.json` so data persists across sessions.
- **Clear Prompts & Feedback**: Informative confirmation messages, error handling, and input validation.

---

## Project Structure
```
/todo_app
│── todo.py          # Main application logic & CLI loop
│── tasks.json       # JSON file storing task records
└── README.md        # Complete user documentation
```

---

## Environment & Requirements
- **Python**: Python 3.x installed on your machine.
- **Dependencies**: Standard library only (`json`, `os`, `sys`).

---

## How to Run the Application

1. Open your command terminal.
2. Navigate to the project directory:
   ```bash
   cd /path/to/todo_app
   ```
3. Run the main application:
   ```bash
   python todo.py
   ```

---

## Command-Line Interface (CLI) Guide

Upon starting `python todo.py`, the interactive main menu appears:

```
==========================================
      Personal To-Do List Application     
==========================================
1. Add Task
2. View Tasks
3. Edit Task
4. Mark Task Completed
5. Delete Task
6. Exit
```

### Options Overview:

1. **Add Task (`1`)**:
   - Prompts for task **Title**, **Description**, and **Category**.
   - Category defaults to `General` if left empty.
   - Automatically saves to `tasks.json`.

2. **View Tasks (`2`)**:
   - Lists all saved tasks with status tags (`[Completed]` / `[Pending]`), category, title, and description.

3. **Edit Task (`3`)**:
   - Enter the task number to edit.
   - Modify title, description, or category. Pressing `Enter` keeps the current value unchanged.

4. **Mark Task Completed (`4`)**:
   - Enter the task number to mark as completed (`[X]`).

5. **Delete Task (`5`)**:
   - Enter the task number to remove the task permanently from `tasks.json`.

6. **Exit (`6`)**:
   - Saves all task changes and exits cleanly.

---

## Testing & Verification

To verify file persistence and application behavior:
1. Launch `python todo.py`.
2. Add a new task with category `Urgent`.
3. View tasks to confirm it appears in the list.
4. Exit the application (Option `6`).
5. Open `tasks.json` to verify the JSON entry was written.
6. Re-launch `python todo.py` and view tasks to ensure persistent loading works correctly.
