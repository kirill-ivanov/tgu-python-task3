import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# авторизация
def loginUser():
    try:
        url = 'https://dummyjson.com/auth/login'
        headers = {"Content-Type": "application/json"}
        data = {
            'username': 'emilys',
            'password': 'emilyspass'
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            user_id = result['id']
            access_token = result['accessToken']

            logging.info(f'Пользователь {user_id} авторизован успешно')
            return user_id, access_token
        else:
            logging.error(f'При авторизации пользователя {data['username']} произошла ошибка')
            raise PermissionError(f"Неправильный логин/пароль у паользователя {data['username']} ")
    except Exception as e:
        logging.error(f'При авторизации пользователя произошла ошибка: {e}')
        raise e


# Обновить информацию по пользователю id с token
def updateUser(id, accessToken):
    try:
        url = 'https://dummyjson.com/users/' + str(id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + accessToken

        }
        data = {
            "lastName": "UpdatedLastName"
        }

        response = requests.put(url, headers=headers, json=data)
        logging.info(f'Данные пользователя {id} обновлены')
    except Exception as e:
        logging.error(f'Ошибка при обновлении пользователя: {e}')
        raise e


# Получение информации по пользователю id с кодом доступа
def getUser(id, accessToken):
    try:
        url = 'https://dummyjson.com/users/' + str(id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + accessToken
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            logging.info(f'{result['firstName']} {result['lastName']} {result['maidenName']}')
        else:
            logging.error(f'При получении информации по пользователю {id} возникла ошибка')
    except Exception as e:
        logging.error(f'Ошибка при получении информации по  пользователю: {e}')
        raise e


id, access_token = loginUser()
updateUser(id, access_token)
getUser(id, access_token)