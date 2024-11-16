import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Получаем список дел и подсчитываем дела со статусом completed = True
def getCalcTodos():
    try:
        count = 0

        url = 'https://dummyjson.com/todos'
        response = requests.get(url)
        if response.status_code == 200:
            for todo in response.json()['todos']:
                if todo['completed']:
                    count += 1
            logging.info(f"Количество выполненных дел: {count}")
        else:
            raise RuntimeError(f'{response.status_code}: {response.text}')
    except Exception as e:
        logging.error(f'При сборе статистики по todo произошла ошибка: {e}')
        raise e


getCalcTodos()
