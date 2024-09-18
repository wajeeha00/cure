import functions as f

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        task = user_action[4:]
        todos = f.get_todos()
        todos.append(task+'\n')
        f.write_todos(todos)

    elif user_action.startswith("show"):
        todos = f.get_todos()
    
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")
                    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            new_task = input("Please Enter New Task: ")

            todos = f.get_todos()
            todos[number] = f"{new_task}\n"

            f.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number")
    
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number -= 1
            todos = f.get_todos()
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            f.write_todos(todos)
            message =  f"To-Do {todo_to_remove} was removed from the list"
        except IndexError:
            print("There is no item with that number")
            continue
    
    elif user_action.startswith("exit"):
        break

    else:
        print("Input is not valid!")

print("Bye!")