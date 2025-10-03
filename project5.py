#To-Do List Application

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter your new task")
    tasks.append(task)
    print(f"Task '{task}' added sucessfully!")

def view_tasks():
    if not tasks:
        print("No taks available. Start adding some")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
                  
def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to update"))
            if 1<= task_num <= len(tasks):
                new_task = input("Enter the new task:")
                old_task =  tasks[task_num - 1]
                tasks[task_num - 1] = new_task
                print(f"Task '{old_task}' updated to '{new_task}'")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete:"))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' delete successfully")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please enter a valid number")

while True:
    show_menu()
    choice = input("Enter your choice (1-5)")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print(" Exiting TO-DO LIST. Good Bye")
        break
    else:
        print("Invalid choice! Please enter a valid number between 1 and 5")