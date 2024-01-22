def add_task(tasks, description):
    task_id = len(tasks) + 1
    tasks[task_id] = {'description': description, 'completed': False}
    print(f"Task added with ID: {task_id}")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")

def complete_task(tasks, task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task {task_id} not found.")

def show_tasks(tasks):
    for task_id, task_info in tasks.items():
        print(f"ID: {task_id}, Description: {task_info['description']}, Completed: {task_info['completed']}")

def main():
    tasks = {}
    while True:
        print("\nOptions: add, delete, complete, show, exit")
        option = input("Enter an option: ").strip().lower()

        if option == 'add':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif option == 'delete':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif option == 'complete':
            task_id = int(input("Enter task ID to complete: "))
            complete_task(tasks, task_id)
        elif option == 'show':
            show_tasks(tasks)
        elif option == 'exit':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
