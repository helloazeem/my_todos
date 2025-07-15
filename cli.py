#from functions import read_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True: # Removed the extra space before this line
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = functions.read_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.read_todos()
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        todos = functions.read_todos()
        try:
            number = int(user_action[5:]) - 1
            if 0 <= number < len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number] = new_todo
                functions.write_todos(todos)
                print("Todo updated successfully.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

        except IndexError:
            print("That number in out of range")

    elif user_action.startswith("complete"):
        todos = functions.read_todos()
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos) #pass the todos to write

            print(f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print(f"There is no item with that number.")

        # Show remaining todos
        print("\nRemaining Todos:")
        for i, item in enumerate(todos, start=1):
            print(f"{i}. {item.strip()}")

    elif user_action.startswith("exit"):
        print("Bye")
        break

    else:
        print("Command is not valid.")

print("Done")

