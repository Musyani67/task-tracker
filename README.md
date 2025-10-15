# Task Tracker

A small command-line task tracker that stores tasks in `tasks.json` in the current directory. Tasks have a description, status (to-do, in-progress, done), a creation timestamp and an updated timestamp.

## Files

- `main.py` — entry point. Uses positional arguments to run actions.

- `arguments.py` — command implementations and formatting helpers.

- `exFunc.py` — helper functions for displaying tasks (uses `tabulate`).

- `jsonSt.py` — JSON file creation/read/write utilities.

- `tasks.json` — example storage file (created automatically when you run the program if missing).

- `requirements.txt` — Python dependency list (`tabulate`).

## Quick setup

1. Use Python 3.8+ (or your system Python 3).

2. Install dependencies (recommended in a virtualenv):

```bash
python3 -m pip install -r requirements.txt
```

How to run

Run the program from the `task-tracker` directory. The usage is:

```bash
python3 main.py <command> <details> [update_info]
```

Where:

- `<command>` is one of: `add`, `update`, `delete`, `mark-done`, `mark-in-progress`, `list`.

- `<details>` meaning depends on the command (see examples below).

- `[update_info]` is optional and used by `update` to supply the new description.

## Commands and examples

- Add a task:

```bash
python3 main.py add "Buy groceries"
# -> adds a new task and prints: Task with ID: 1 added successfully ✅
```

- Update a task's description (use the task ID as the details):

```bash
python3 main.py update 2 "Finish coding exercise"
# -> updates task with ID "2" to the new description
```

- Delete a task by ID:

```bash
python3 main.py delete 3
```

- Delete all tasks:

```bash
python3 main.py delete all
```

- Mark a task done:

```bash
python3 main.py mark-done 1
```

- Mark a task in-progress:

```bash
python3 main.py mark-in-progress 1
```

- List tasks:

```bash
# List everything
python3 main.py list all

# List by status (one of: to-do, in-progress, done)
python3 main.py list done
```

That's it — run `python3 main.py list all` to see current tasks and start adding new ones.

## PROJECT'S URL

<https://roadmap.sh/projects/task-tracker>
