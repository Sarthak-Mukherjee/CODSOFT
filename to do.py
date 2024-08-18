def main():
   
    while True:
        print("----To Do App----")
        print("1.Add Task Description\n2.View Task(s)\n3.update task(s)\n4.delete task(s)\n5.Exit")
        ch=input("Enter your choice:")
        if ch=='1':
            add_task()
        elif ch=='2':
            view_task()
        elif ch=='3':
            update_task()
        elif ch=='4':
            delete_task()
        elif ch=='5':
            print("Thank You! Exiting your To Do App.")
            exit(0)
        else:
            print("Invalid Input.Please provide a valid choice.")
            continue
tasks=[]



def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully!")

def view_task():
     
    print("Your To Do list is")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    view_task()
    try:
        index=int(input("Enter the number of task you want to update:"))-1
        new_desc=input("Enter the new task description:")
        tasks[index]=new_desc
        print("Updated Successfully!")
    except(ValueError,IndexError):
        print("Enter a valid task number.")

def delete_task():
    view_task()
    try:
        index=int(input("Enter task number that you want to do delete:"))-1
        delete_task=tasks.pop(index)
        print("Task Deleted Successfully!")
    except(ValueError,IndexError):
        print("Enter a valid task number.")

if __name__ == "__main__":
    main()