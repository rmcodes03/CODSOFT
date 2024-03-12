tasks = []

def addTask():
    entertask = input("\n> Enter the task: ")
    tasks.append(entertask)
    print("> Task added to the list")

def showTasks():
    if len(tasks) == 0:
        print("\n> There are no tasks.")
    else:
        print("\n> Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def deleteTask():
    showTasks()
    if len(tasks) > 0:
        delete_task_no = int(input("\n> Enter the task number to be deleted: "))
        if delete_task_no >= 1 and delete_task_no <= len(tasks):
            tasks.pop(delete_task_no-1)
            print(f"> Task {delete_task_no} deleted.")
        else:
            print(f"> Invalid input. Task {delete_task_no} does not exist.")

def updateTask():
    showTasks()
    if len(tasks) > 0:
        update_task_no = int(input("\n> Enter the task number to be updated: "))
        if update_task_no >= 1 and update_task_no <= len(tasks):
            tasks[update_task_no-1] = input("> Update the task: ")
            print(f"> Task {update_task_no} updated.")
        else:
            print(f"> Invalid input. Task {update_task_no} does not exist.")

while True:
    print("---------------------------------------------------------")
    print("1. Add task")
    print("2. Delete task")
    print("3. Update task")
    print("4. Show tasks")
    print("5. Quit")
    choice = int(input("\n> Choose any one of the above options: "))

    if choice >= 1 and choice <= 5:
        if choice == 1:
            addTask()
        elif choice == 2: 
            deleteTask()
        elif choice == 3:
            updateTask()
        elif choice == 4:
            showTasks()
        elif choice == 5:
            break
    else:
        print("> Invalid input. Enter number between 1-5.")
