from task_manager import TaskManger

def main():
    manager = TaskManger("/Users/ajitchandran/Desktop/pyOps/taskManager/tasks.json")
    while True: # if while true means it will keep looping right? how deos it stops?
        print("\nTask Manager")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)
        elif choice == "2":
            manager.read_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (or leave blank): ")
            description = input("Enter new description (or leave blank): ")
            completed = input("Mark as completed? (yes/no): ").lower() == "yes"
            manager.update_task(task_id, title or None, description or None, completed) #what is the technical term for assigning or None ?
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__": # explain this __name__ == "__main__"
    main()