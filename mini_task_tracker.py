import json
from pathlib import Path

# Name of the JSON file used to store tasks.
TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Load saved tasks from the JSON file, or return an empty list."""
    try:
        # Open the existing file and convert its JSON data into a Python list.
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        # Check that the loaded data has the expected list structure.
        if not isinstance(tasks, list):
            print("Warning: tasks.json does not contain a task list. Starting empty.")
            return []

        return tasks

    except FileNotFoundError:
        # The first time the program runs, the file may not exist yet.
        return []
    except json.JSONDecodeError:
        # Handle a file that exists but does not contain valid JSON.
        print("Warning: tasks.json is invalid. Starting with an empty task list.")
        return []
    except OSError:
        # Handle other file-reading problems without crashing.
        print("Warning: Could not read tasks.json. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    try:
        # Write the latest task list to disk in readable JSON format.
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks. Check file permissions or storage.")


def add_task(tasks):
    """Ask for a title and add a new pending task."""
    title = input("Task title: ").strip()

    # Do not allow a blank or whitespace-only title.
    if not title:
        print("Task title cannot be empty.")
        return

    # Each task is stored as a dictionary with a title and completion status.
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Display all tasks with their numbers and status."""
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        # Display Done for completed tasks and Pending for unfinished tasks.
        status = "Done" if task.get("done", False) else "Pending"
        print(f"{number}. {task.get('title', 'Untitled')} [{status}]")


def get_task_index(tasks, action):
    """Ask for a task number and return its zero-based index, or None."""
    if not tasks:
        print(f"There are no tasks to {action.lower()}.")
        return None

    try:
        # The user sees task numbers starting at 1, but list indexes start at 0.
        task_number = int(input(f"Task number to {action.lower()}: "))
    except ValueError:
        print("Invalid number. Please enter a whole number.")
        return None

    # Reject numbers outside the range of the current task list.
    if task_number < 1 or task_number > len(tasks):
        print(f"Invalid task number. Enter a number from 1 to {len(tasks)}.")
        return None

    return task_number - 1


def complete_task(tasks):
    """Mark a selected task as completed."""
    index = get_task_index(tasks, "complete")
    if index is None:
        return

    # True means the task is complete.
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove a selected task from the list."""
    index = get_task_index(tasks, "delete")
    if index is None:
        return

    # Remove the selected task using its list index.
    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed_task.get('title', 'Untitled')}")


def main():
    """Run the menu until the user chooses Exit."""
    # Load previously saved tasks when the program starts.
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add   2. View   3. Complete   4. Delete   5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            # Save once more before leaving, then stop the loop.
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            # Handle menu choices other than 1, 2, 3, 4, or 5.
            print("Invalid choice. Please select a number from 1 to 5.")


# Run the menu only when this file is executed directly.
if __name__ == "__main__":
    main()
