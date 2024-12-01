import pytest


from task_manager import TaskManager


def test_add_task():
    task_manager = TaskManager('test_tasks.json')
    task_manager.add_task("Test Task", "This is a test task", "Work", "2024-12-01", "High")
    assert len(task_manager.tasks) == 1


def test_complete_task():
    task_manager = TaskManager('test_tasks.json')
    task_manager.add_task("Test Task", "This is a test task", "Work", "2024-12-01", "High")
    task_manager.complete_task(task_manager.tasks[0].id)
    assert task_manager.tasks[0].status is True


def test_delete_task():
    task_manager = TaskManager('test_tasks.json')
    task_manager.add_task("Test Task", "This is a test task", "Work", "2024-12-01", "High")
    task_id = task_manager.tasks[0].id
    task_manager.delete_task(task_id)
    assert len(task_manager.tasks) == 0