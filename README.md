# Задание
```
Требуется разработать API-сервис для получения данных о первых 10 объявлениях по ссылке https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/ .
Для решения задачи необходимо:
Разработать модели при помощи фреймворка Django/FastAPI со следующими полями:
заголовок объявления;
id объявления;
автор объявления;
количество просмотров объявления;
позиция, на которой стоит объявление.
	Данные могут быть добавлены в БД вручную или любым удобным для вас способом.
Разработать методы API для обращения к данным моделям. Запрос к API должен иметь параметр ID. При обращении, API должен возвращать информации об объявлении с ID, переданным в запросе, в формате JSON.
Требования к реализации API:
При разработке должен быть использован язык Python и фреймворк Django/FAST Api.
В качестве результата должен быть предоставлен репозиторий на GitHub;
Сервис должен использовать принципы ООП.
Дополнительные требования, не обязательны к выполнению, но будут являться большим плюсом:
Реализована система регистрации и входа (верификации аккаунта) для подключения к API (без функционала смены и/или восстановления пароля);
Все обращения к базе данных должны быть реализованы при помощи ORM запросов.
```

### **Запуск проекта в dev-режиме**
1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/SobrSergio/DjangoAPI.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 

```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграцию:
```
python manage.py makemi​gra​tions
python manage.py migrate
```

5. Запустите команду для сбора данных и наполнение БД
```
cd api_service
python manage.py fetch_ads 
```

6. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

# Как пользоваться!
### Примеры использования API

Регистрация нового пользователя
```
curl -X POST http://localhost:8000/api/register/ -H "Content-Type: application/json" -d '{"username": "newuser", "password": "newpassword", "email": "newuser@example.com"}'
```

Получение JWT токена
```
curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "newuser", "password": "newpassword"}'
```

Обновление JWT токена
```
curl -X POST http://localhost:8000/api/token/refresh/ -H "Content-Type: application/json" -d '{"refresh": "your_refresh_token"}'
```
Доступ к защищенному API
```
curl -X GET http://localhost:8000/api/ads/1/ -H "Authorization: Bearer your_access_token"
```

Адрес запроса - http://localhost:8000/api/ads/1/.
Последняя цифра представляет собой идентификатор объявления от 1 до 10.
В случае если его не писать, выходят все объявления.

## Почему такая реализация
Команда python manage.py fetch_ads вызывает парсер для сбора данных. Можно автомотизировать этот процесс разными способами. В случаче, если он не работает, это связано с тем, что у вас не установлен driver для selenium. Так же в случае ммногочисленных запросов на сайт, может появиться ReCaptcha. (обходить сложно и процесс сбора данных будет долгим, об этом в задании не сказано)
Регистрацию пользователей сделал максимально интересную, чтобы показать мои знания библиотеки DJANGO. Пользоваться могут все, кто зарегистрируются и получат ТОКЕН.

