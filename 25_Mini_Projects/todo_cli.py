# Python Basics to Advanced Example
# Run: python todo_cli.py

tasks = []
while True:
    command = input("add/list/done/quit: ").strip().lower()
    if command == "add": tasks.append({"task": input("Task: "), "done": False})
    elif command == "list":
        for i, task in enumerate(tasks, 1): print(i, "[x]" if task["done"] else "[ ]", task["task"])
    elif command == "done":
        try: tasks[int(input("Task number: "))-1]["done"] = True
        except (ValueError, IndexError): print("Invalid task number")
    elif command == "quit": break
    else: print("Unknown command")
