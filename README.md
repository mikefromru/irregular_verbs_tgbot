# Телеграм бот (Неправильные глаголы)
<i>Бот разработан для изучения неправильных глаголов в английском языке.</i>

>Реализована функция отправки сообщения на email когда новый пользователь запускает бота

### Используемые технологии
- Python3.11
- Aiogram
- Docker

### Начать
1. Клонировать репозиторий
```
git clone https://github.com/mikefromru/irregular_verbs_tgbot.git
```
2. Перейти в папку проекта
```
cd irregular_verbs_tgbot
```
3. Создать виртуальное окружение
```
python3.11 -m venv venv
```
4. Активировать виртуальное окружение
```
source venv/bin/activate
```
5. Установить зависимости
```
python install -r requirements.txt
```
6. Переименовать json_files.EXAMPLE в json_files
7. Создать `.env` файл в корне проекта
```
TOKEN=your_token_from_telegram
RECIPIENTS='["emai_for_getting_messages_who_run_the_bot@yandex.ru"]'
GMAIL_USER=your_email_gmail@gmail.com
GMAIL_PASSWORD=your_password
```
8. Запустить бота
```
python main.py
```

