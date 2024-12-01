from task import Task
from task_manager import TaskManager


def main():
    task_manager = TaskManager('tasks.json')

    while True:
        print("\n1. Просмотр задач")
        print("2. Добавление задачи")
        print("3. Изменение задачи")
        print("4. Удаление задачи")
        print("5. Поиск задач")
        print("6. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            for task in task_manager.list_tasks():
                print(task.to_dict())
        elif choice == '2':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = input("Введите срок выполнения (YYYY-MM-DD): ")
            priority = input("Введите приоритет (низкий/средний/высокий): ")
            task_manager.add_task(title, description, category, due_date, priority)
        elif choice == '3':
            task_id = input("Введите ID задачи для редактирования: ")
            task_manager.complete_task(task_id)
        elif choice == '4':
            task_id = input("Введите ID задачи для удаления: ")
            task_manager.delete_task(task_id)
        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска: ")
            tasks = task_manager.search_tasks(keyword)
            for task in tasks:
                print(task.to_dict())
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()