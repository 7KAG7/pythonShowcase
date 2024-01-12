class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

# Create an instance of TodoList
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Complete Python project")
todo_list.display_tasks()  

# Command-line interface loop
while True:
    print("\n1. Add Task\n2. Display Tasks\n3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == '2':
        todo_list.display_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")

def main():
    # Create an instance of TodoList
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Complete Python project")
    todo_list.display_tasks()

if __name__ == "__main__":
    main()