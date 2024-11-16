import json

import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Добавление одного дела
def addTodo(todo, userId):
    try:
        url = 'https://dummyjson.com/todos/add'
        data = {
            'todo': todo,
            'completed': False,
            'userId': userId,
        }

        response = requests.post(url, data=data)
        if response.status_code == 201:
            id = response.json()['id']
            logging.info(f"Задание {id} создано")
            return id
        else:
            raise RuntimeError(f'{response.status_code}: {response.text}')
    except Exception as e:
        logging.error(f'При создании задания произошла ошибка: {e}')
        raise e


# Список дел, которые нужно добавить
todo_list = ["Read a book", "Write unit tests", "Update documentation"]

# В этот массив будем сохранять ID сохраненных дел
todo_result_id = []

for todo in todo_list:
    todo_result_id.append(addTodo(todo, 1))
print(todo_result_id)
