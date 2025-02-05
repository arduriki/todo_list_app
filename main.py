while True:
    # .strip()
    # if the user adds a whitespace in the command
    # the program will still be able to know the command
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            # To read what's inside the .txt file
            file = open("todos.txt", "r")
            # Create a list from the file
            # usually we won't create a list per se...
            todos = file.readlines()
            # Always close when you're done
            file.close()
            todos.append(todo)
            # Store todos in a file, in write mode
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            # Read the file
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            # Delete the '\n' from the list
            # Method 1 - Using a 'for-loop'
            # new_todos = []
            # for todo in todos:
            #     new_todo = todo.strip("\n")
            #     new_todos.append(new_todo)

            # Method 2 - Using FP
            # new_todos = [todo.strip("\n") for todo in todos]

            # Method 3
            # Go through the file
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: ")) - 1
            todos.pop(number)
        case "exit":
            break

print("Bye!")
