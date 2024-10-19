import requests

def authenticate_user(user_key):
    api_url = 'http://flask-rouge-seven.vercel.app/api/auth'  # Замените на URL вашего API

    try:
        # Отправка POST-запроса с ключом пользователя
        response = requests.post(api_url, json={'key': user_key})

        if response.status_code == 200:
            # Успешная аутентификация
            data = response.json()
            print('Аутентификация успешна!')
            print('Данные пользователя:', data['user_data'])
            print('Сообщение:', data['message'])
        else:
            # Обработка ошибок
            error_data = response.json()
            print('Ошибка аутентификации:', error_data['error'])
    except Exception as e:
        print('Ошибка при выполнении запроса:', e)

if __name__ == '__main__':
    # Запрашиваем ключ у пользователя
    user_key = input("Введите ваш ключ: ")
    authenticate_user(user_key)
