from typing import List, Optional
from task import Task

class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def delete_task(self, t_id: int) -> None:
        self.tasks = [task for task in self.tasks if task.t_id != t_id]
    
    def get_task(self, t_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.t_id == t_id:
                return task
    
    def edit_task_description(self, t_id: int, new_description: str) -> None:
        task: Task = self.get_task(t_id)
        if task:
            task.change_description(new_description)
    
    def edit_task_state(self, t_id: int, new_state: str) -> None:
        task: Task = self.get_task(t_id)
        if task:
            task.change_state(new_state)
