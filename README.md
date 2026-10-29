# Mini Task Tracker

## Project goal
A beginner-friendly, menu-based Python task tracker that saves tasks in a JSON file and reloads them when the program starts.

## Features
- Add a task with a title; new tasks start as **Pending**.
- View a numbered list of tasks with **Pending** or **Done** status.
- Mark a task as completed.
- Delete a task.
- Save tasks to `tasks.json` with `json.dump()`.
- Load saved tasks at startup with `json.load()`.
- Handle blank titles, invalid menu choices, invalid task numbers, and a missing or invalid JSON file.

## Requirements
Python 3.6 or newer. No external packages are required.

## How to run
1. Keep `mini_task_tracker.py` in a folder where you want `tasks.json` to be stored.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python mini_task_tracker.py
   ```

4. Use the menu:
   - `1` Add
   - `2` View
   - `3` Complete
   - `4` Delete
   - `5` Exit

The `tasks.json` file is created when tasks are saved. Keep it in the same folder as the Python script so the program can reload your tasks on the next run.

## Example
```text
--- TASK TRACKER ---
1. Add   2. View   3. Complete   4. Delete   5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2

Your tasks:
1. Read notes [Pending]
```

## Files
- `mini_task_tracker.py` — Python source code.
- `tasks.json` — created automatically when the program saves tasks.

## Suggested GitHub commit plan
1. `Add task tracker core menu and JSON persistence`
2. `Improve validation and document usage`

