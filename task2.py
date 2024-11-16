import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Создаем продукт
# Return ID
def addProduct():
    url = 'https://dummyjson.com/products/add'
    data = {
        'title': 'Test Product"',
        'description': 'This is a test product',
        'price': 99
    }

    response = requests.post(url, data=data)
    id = response.json()['id']
    logging.info(f'Создан продукт с id = {id}')
    return id


# Удаляем продукт по ID
def deleteProduct(id):
    response = requests.delete('https://dummyjson.com/products/' + str(id))
    logging.info(f'Удален продукт с id = {id}')


# Проверка на отсутствие продукта с таким ID
def checkHasNot(id):
    try:
        response = requests.get('https://dummyjson.com/products/' + str(id))
        if response.status_code == 404:
            return True
        else:
            return False;
    except Exception as e:
        print(f'Произошла ошибка{e}')
        logging.error(f'При проверке наличия продукта произошла ошибка{e}')

try:
    id = addProduct()
    deleteProduct(id)

    if checkHasNot(id):
        logging.info(f'Продукт {id} был удален успешно')
    else:
        logging.info(f'Продукт {id} не был удален')
except Exception as e:
    logging.error(f'Произошла ошибка{e}')
