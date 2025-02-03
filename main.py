todos = []

while True:
    # .strip()
    # if the user adds a whitespace in the command
    # the program will still be able to know the command
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
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
