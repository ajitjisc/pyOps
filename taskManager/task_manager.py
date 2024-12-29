from task import Task
from storage import Storage


class TaskManger:
    def __init__(self, storage_path):
        self.storage = Storage(storage_path)
        self.tasks = self.storage.load_tasks() 
        # why self.storage.load_tasks(), why not Storage.load_tasks() ?
        # what is self.tasks? why it is being used in differnt functions below?
    
    def create_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)
        print(f"Task '{title}' created successfully.")
        
    
    def read_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.task_id}: {task.title} - {task.description} [{status}]")
            # why status in []?
    
    
    def update_task(self, task_id, title=None, description=None, completed = None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if completed is not None:
                    task.completed = completed
                self.storage.save_tasks(self.tasks)
                print(f"Task {task_id} updated successfully")
                return
        print(f"Task {task_id} not found")
    # why in each function we have self argument?
    # why we have a return after self.storage.save_tasks(self.tasks) ?
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage.save_tasks(self.tasks)
        print(f"Task {task_id} deleted successfully")