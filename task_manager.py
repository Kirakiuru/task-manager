import json
import os

from task import Task

class TaskManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return [Task(**task) for task in json.load(file)]
        return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def add_task(self, title, description, category, due_date, priority):
        task = Task(title, description, category, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_completed()
                self.save_tasks()
                return

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    def get_tasks_by_category(self, category):
        return [task for task in self.tasks if task.category == category]

    def list_tasks(self):
        return self.tasks
