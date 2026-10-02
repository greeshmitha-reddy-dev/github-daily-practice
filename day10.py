# Day 10 - Python To-Do List Manager

tasks = []


def add_task():

    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "status": "Pending"
    }

    tasks.append(task)

    print("Task added successfully!")


def view_tasks():

    if len(tasks) == 0:

        print("No tasks found.")

        return

    print()
    print("========== TO-DO LIST ==========")

    for number, task in enumerate(tasks, start=1):

        print(
            number,
            ".",
            task["task"],
            "-",
            task["status"]
        )


def complete_task():

    if len(tasks) == 0:

        print("No tasks available.")

        return

    view_tasks()

    task_number = int(input("Enter task number to complete: "))

    if task_number >= 1 and task_number <= len(tasks):

        tasks[task_number - 1]["status"] = "Completed"

        print("Task completed successfully!")

    else:

        print("Invalid task number.")


def delete_task():

    if len(tasks) == 0:

        print("No tasks available.")

        return

    view_tasks()

    task_number = int(input("Enter task number to delete: "))

    if task_number >= 1 and task_number <= len(tasks):

        deleted_task = tasks.pop(task_number - 1)

        print("Deleted task:", deleted_task["task"])

    else:

        print("Invalid task number.")


while True:

    print()
    print("========== TO-DO LIST MANAGER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        complete_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        print("Thank you for using To-Do List Manager!")

        break

    else:

        print("Invalid choice. Please try again.")