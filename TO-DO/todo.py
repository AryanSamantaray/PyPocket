Tasks=[]


while True:
    print("=== TODO LIST ===")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Quit")
    choice = input("Choose an option: ")
    print("You chose:", choice)
    if choice == "1":
        print(Tasks)
    if choice == "2":
        Task=input("What do you need to do ?")
        Tasks.append(Task)
    if choice == "3":
            print("Goodbye!")
            break
