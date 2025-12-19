def display_menu():
    print("to-do list application")
    print("1. view task")
    print("2. add tasks")
    print("3. remove tasks")
    print("4. exit")

def view_task(tasks):
    if not tasks:
        print("no tasks avialable.")
    else:
        print("your tasks :")
        for i, task in enumerate(tasks, start = 1):
            print (f"{i}. {task}")

def add_task(tasks):
    task = input ("enter the task you want to add:")
    if task :
        tasks.append(task)
        print (f"task '{task}' added successfully.")
    
def remove_task(tasks):
    view_task(tasks) 
    try:
        task_number = int(input("enter the task number to delete:"))
        if 1 <= task_number <= len(tasks):
            remove_task = tasks.pop(task_number - 1)
            print(f"task '{remove_task}' removed successfully.")
        else:
            print("invallid task number. please  try again.")
    except ValueError:
        print ("invalid input. please enter a valid task number.")


def to_do_list():
    tasks = []
    while True:
        display_menu()
        choice = input("enter your choice (1-4): ")
        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print ("exiting the application. goodbye!!!")
            break
        else :
            print("invalid choice. please try again.")

to_do_list()



    
