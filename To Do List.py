class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{idx}. [{status}] {task['task']}")
    
    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index.")
    
    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

# Create a to-do list
todo_list = ToDoList()

print("Welcome to the To-Do List Simulation!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Remove Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
        print("Task added.")
    elif choice == '2':
        print("Tasks:")
        todo_list.view_tasks()
    elif choice == '3':
        task_idx = int(input("Enter the task index to mark as completed: ")) - 1
        todo_list.mark_completed(task_idx)
        print("Task marked as completed.")
    elif choice == '4':
        task_idx = int(input("Enter the task index to remove: ")) - 1
        todo_list.remove_task(task_idx)
        print("Task removed.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
