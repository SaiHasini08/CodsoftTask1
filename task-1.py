tasks = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append({"name": task, "status": "Pending"})
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["name"], "|", tasks[i]["status"])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            try:
                num = int(input("Enter task number to mark as done: "))
                if num < 1 or num > len(tasks):
                    print("Invalid task number!")
                else:
                    tasks[num - 1]["status"] = "Done"
                    print("Task marked as done!")
            except:
                print("Please enter a valid number!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if num < 1 or num > len(tasks):
                    print("Invalid task number!")
                else:
                    tasks.pop(num - 1)
                    print("Task deleted!")
            except:
                print("Please enter a valid number!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
