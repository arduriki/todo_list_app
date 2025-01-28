todos = []

while True:
    # .strip()
    # if the user adds a whitespace in the command
    # the program will still be able to know the command
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            break
        case _:
            print("Sorry, enter a valid command")

print("Bye!")