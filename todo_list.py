import os


def show_todo(todos):
    if not todos:
        print("No to-do list found..!!")
    else:
        for i, todo in enumerate(todos, 1):
            print(f"{i}.{todo}")


def add_todo(todos, new_todos):
    todos.append(new_todos)
    print("New to-do list added successfully..!!!")


def update_todo(todos, index, updated_todo):
    if 1 <= index <= len(todos):
        todos[index - 1] = updated_todo
        print("To-do list updated successfully....!!!")
    else:
        print("Invalid to-do list index...")


def delete_todo(todos, index):
    if 1 <= index <= len(todos):
        delete_todo = todos.pop(index - 1)
        print(f"To-do list '{delete_todo}' deleted successfully...!!!")
    else:
        print("Invalid to-do list...")


def save_todo_to_file(file_path, todos):
    with open(file_path, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")


def load_todo_from_file(file_path):
    todo = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            todo = file.read().splitline()
    return todo


def main():
    file_path = "todo_lst.txt"
    todos = load_todo_from_file(file_path)
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Show To-do List")
        print("2. Add To-do List")
        print("3. Update To-do List")
        print("4. Delete To-do List")
        print("5. Save and Exit")
        choice = input("Enter your choice from 1 to 5: ")
        if choice == "1":
            show_todo(todos)
        elif choice == "2":
            new_todo = input("Enter the task: ")
            add_todo(todos, new_todo)
        elif choice == "3":
            index = int(input("Enter the todo number to update: "))
            updated_todo = input("Enter the update todo: ")
            update_todo(todos, index, updated_todo)
        elif choice == "4":
            index = int(input("Enter the todo number to delete: "))
            delete_todo(todos, index)
        elif choice == "5":
            save_todo_to_file(file_path, todos)
            print("Todo saved. Exiting....")
            break
        else:
            print("Invalid choice. Please do again.")


if __name__ == "__main__":
    main()
