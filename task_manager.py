import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task():
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks = load_tasks()
    new_id = max([task['id'] for task in tasks], default=0) + 1
    tasks.append({
        "id": new_id,
        "title": title,
        "due_date": due_date,
        "status": "pending"
    })
    save_tasks(tasks)
    print("Task added.")

def view_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['id']}: {task['title']} (Due: {task['due_date']}) - {task['status']}")

def mark_completed():
    task_id = int(input("Enter task ID to mark as completed: "))
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            break
    save_tasks(tasks)
    print("Task updated.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Completed\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
