import json
from task import Task

class Storage:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []
    
    def save_tasks(self, tasks):
        with open(self.file_path, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)