# Проект QRkot

## Описание проекта:

Проект **QRkot** представляет собой представляет приложение для Благотворительного фонда, реализованное на фреймворке FastAPI.

Фонд **QRKot** имеет возможность запускать несколько конкретных проектов одновременно. Каждый из этих проектов имеет своё уникальное название, описание своей цели и требуемую сумму средств для реализации. Как только необходимая сумма собирается для определенного проекта, он считается завершенным и закрывается.

Система сбора пожертвований в этих проектах основана на принципе *First In, First Out*. Все пожертвования направляются в проект, который был запущен раньше других. Как только этот проект достигает требуемой суммы и завершается, пожертвования начинают направляться в следующий по порядку проект.

### Возможности сервиса:

- Создание проектов для сбора денег,
- Автоматическое распределение взносов от участников между созданными проектами,
- Управление участниками системы,
- Создание сводных отчетов о завершенных проектах с использованием Google Таблиц.

### Документация проекта:

После запуска сервиса докуменация доступна по адресам `/docs` и `/redoc`

### База данных:

В рамках проекта настроено взаимодействие с базой данных через **ORM SQLAlchemy**. Миграции базы данных настроены с использованием библиотеки **Alembic**.

### Создание отчетов в google таблице:
#### Для взаимодейстивия с GoogleAPI необходимо:
1. Создайте проект в Google Cloud Platform.
2. Настройте проект с использованием сервисного аккаунта и активируйте Google Drive API и Google Sheets API.
3. Сгенерируйте JSON-файл с учетными данными сервисного аккаунта.
4. Сохраните учетные данные в файл .env для дальнейшего использования.
5. Добавить в файл .env адрес личного гугл-аккаунта для выдачи прав доступа к сформированному отчету.

## Технологии проекта:

- Python 3.9
- FastAPI 0.78.0
- Uvicorn 0.17.6
- SQLAlchemy 1.4.36
- Alembic 1.7.7
- FastAPI Users 10.0.4
- Aiogoogle 4.2.0
- Google Sheet API v4
- Google Drive API v3

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:alekseikoznov/QRkot.git
```

```
cd QRkot
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
4. Создать файл .env с переменными окружения. Пример наполнения:

```
APP_TITLE=
APP_DESCRIPTION=
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=SECRET
FIRST_SUPERUSER_EMAIL=
FIRST_SUPERUSER_PASSWORD=
EMAIL=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY="..."
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
```
5. Создать базу данных:
```
$ alembic upgrade head
```
6. Запустить приложение:
```
$ uvicorn app.main:app
```
