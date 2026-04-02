tasks=[]

try:
    with open("tasks.txt","r") as f:
        tasks=[line.strip() for line in f]
except:
    tasks=[]

def add_task():
    task=input("Enter Task ")
    tasks.append(task)
    save_task()
    print("Task Added")

def view_task():
    if not tasks:
        print("No Tasks")
    else:
        for i, task in enumerate(tasks):
            print(i+1,task)

def delete_task():
    view_task()
    num=int(input("Enter a task number to delete "))
    if 0<num<= len(tasks):
        tasks.pop(num-1)
        save_task()
        print("Task Deleted")
    
    else:
        print("Invalid number")

def save_task():
    with open("tasks.txt","w") as f:
        for task in tasks:
            f.write(task+"\n")


while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        break
    else:
        print("Invalid choice")