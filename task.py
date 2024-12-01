import uuid
from datetime import datetime


class Task:
    def __init__(self, title, description, category, due_date, priority):
        self.id = str(uuid.uuid4())  # Уникальный идентификатор
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date  # Дата выполнения
        self.priority = priority  # Низкий, средний, высокий
        self.status = False  # Выполнена или нет


    def mark_as_completed(self):
        self.status = True


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }
