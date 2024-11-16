import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Получение постов пользователя
def getPosts(id):
    try:
        url = 'https://dummyjson.com/users/' + str(id) + '/posts'

        response = requests.get(url)
        if response.status_code == 200:
            for post in response.json()['posts']:
                print(post['title'])
            logging.info(f'Данные по пользователю {id} получены успешно')
        else:
            raise RuntimeError(f'{response.status_code}: {response.text}')
    except Exception as e:
        logging.error(f'При авторизации пользователя произошла ошибка: {e}')
        raise e


getPosts(5)
