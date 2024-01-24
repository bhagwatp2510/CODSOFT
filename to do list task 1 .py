tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task name: ")
        tasks.append({"name": task, "completed": False})
        print("Task added !")
    elif choice == 2:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['name']} - {'Completed' if task['completed'] else 'Incomplete'}")
    elif choice == 3:
        index = int(input("Enter task number: ")) - 1
        tasks[index]['completed'] = True
        print("Task marked  completed!")
    elif choice == 4:
        break
    else:
        print("Invalid choice.")