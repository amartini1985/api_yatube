# Описание проекта:

Веб-приложение на Python с использованием Django.

## Используемый стек технологий:
- Python 3.9
- Django
- Django REST Framework

## Порядок развертывания проекта:
1) Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:amartini1985/api_yatube.git
```

```
cd api_final_yatube
```

2) Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

3) Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

4) Запустить проект:

```
python3 manage.py runserver
```



## Cпецификация проекта
Спецификация будет доступна по адресу: http://127.0.0.1:8000/redoc/

## Автор проекта:
[Andrey Martyanov/amartini1985](https://github.com/amartini1985)
