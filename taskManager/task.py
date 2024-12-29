class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        """Convert the task object to a dictionary"""
        return{
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
        
    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary"""
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            completed=data["completed"]
        )
            
        