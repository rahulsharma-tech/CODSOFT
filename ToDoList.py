class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task {index} updated successfully.")
        else:
            print(f"Invalid task index. Please enter a number between 1 and {len(self.tasks)}.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print(f"Invalid task index. Please enter a number between 1 and {len(self.tasks)}.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            index = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)

        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)

        elif choice == '5':
            print("\nExiting To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()







