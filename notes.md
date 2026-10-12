Python мои заметки

23.09.26

*** Основы
- print("текст") - вывести на экран
- input("вопрос") - спррашивает у пользователся, возвращает строку
- int(...) - превратить строку в целое число
f-строки: 'f"Привет, {name}!"' - подставляет перемеенную в скобках

*** Условия
`if условие:` / `elif условие:` / `else - "иначе":' - ветвление
`==` сравнение (два знака!), `=` присваивание (один знак)
`!=` не равно, `>` `<` `>=` `<=`
`and`, `or`, `not` — логика
- Отступ после `:` обязателен

*** Обработка ошибок
`try:` - попробовать выполнить
`except ValueError:` - если ошибка этого типа (то)
`except FileNotFoundError:` - если файла нет
`return` после `except` - чтобы выйти из функции

*** Циклы
`while True: - бесконечный цикл повторения. Выход через `break`
`for i in range(5):` - повторить 5 раз (0, 1, 2, 3, 4)
`for i in range(1, 101):` - значения от 1 до 100
`break` - выйти из цикла
`continue` - пропустить итерацию

*** Файлы
`with open("file.txt", "w") as f:` - открыть на запись (стирает старое)
`with open("file.txt", "r") as f:` - открыть на чтение
`with open("file.txt", "a") as f:` - открыть на добавление
`f.read()` - прочитать всё
`f.readlines()` - прочитатть в список строк
`f.write("текст")` - записать в строку
`with` - сам закрывеаект файл - не нужен `f.close()`
`try / except FileNotFoundError` - если файла нет

*** Функции
`def имя(параметры):`- сама функция/название/параметр
Функция не выполнится, пока её не вызовешь: `имя(аргументы)`
`return` - возвращает значение - можно сохранить в переменную
`print` - просто показывает на экране, ничего не возвращает
`return True` / `return False` - сигнал остновному коду
`if not mark_done(todos):` - «если функция вернула False, то...»

*** Словари
`counts = {}` - пустой словарь
`counts["key"] = value` - добавить или изменить
`counts["key"]` - получить значечние (KeyError, если нет ключа)
`counts.get("key")` - безопасно получить (None, если нет)
`del counts["key"]` - удалить ключ
`"key" in counts` - проверить наличие ключа
`for key, value in counts.items():` - перебор ключей и значений
`len(counts)` - количество пар

*** Списки
`todos = []` - пустой список
`todos.append(x)` - добавить в конец списка
`todos.remove(x)` - Удалить по значению
`todos.pop(0)` - удалить по индексу(ПО НОМЕРУ)
`len(переменная)` - Количество элементов
`x in todos` - Проверка, есть ли X в списке
`enumerate(todos, start=1)` - нумерация  с 1

*** Модули
`import random` - подключить модуль
`random.randint(1, 100)` - случайное число от 1 до 100

*** Мои грабли (важно!)
- Расширение файла должно быть `.py` — не `.py.ru`, не `.py.txt`, не без точки
- Отступы: 4 пробела внутри `while`, 8 внутри `if` внутри `while`
- `break` должен быть **внутри** цикла, иначе `SyntaxError`
- `int("abc")` → `ValueError` — не число
- Разные отступы в одном блоке → `IndentationError`
- Файл `lesson1.ру` — русская раскладка, Python не найдёт

## Git и GitHub
- `git init` — создать репозиторий (один раз)
- `git add .` — добавить все файлы
- `git commit -m "сообщение"` — сохранить версию
- `git push` — залить на GitHub
- `git config --global user.name "Имя"` — настройка имени
- `git config --global user.email "email"` — настройка email
- Personal Access Token — нужен вместо пароля при push
- `git config --global http.sslbackend schannel` — если SSL-ошибка
- Сайт: github.com — там лежит твой проект

*** Ошибки, которые уже ловил
- `NameError` — переменная не определена (забыл кавычки у строки)
- `ValueError` — `int()` получил не число
- `SyntaxError: 'break' outside loop` — сбит отступ
- `IndentationError` — разные отступы в блоке

*** Вопросы (разобрать позже)
- Разница между `print` и `return`
- Когда использовать `while`, а когда `for`
- Что такое функция и зачем `def`
`return True` / `return False` - сигнал остновному коду





*** Что уже умею (итог)
- To-Do с меню: показать / добавить / удалить / выход
- Сохранение дел в файл `todos.txt`
- Счётчик слов через словарь
- Поиск слова в тексте (`find_word`)
- Игра «Угадай число» с random

*** ООП (объектно-ориентированное программирование)

*** Зачем нужно
- Объединяет данные и функции в одну сущность — объект
- Вместо 300 переменных для 100 книг — 100 объектов
- Легко масштабировать, передавать, добавлять поля
- Основа фреймворков: Django, FastAPI, SQLAlchemy — всё на классах

*** Класс и объект
- Класс — чертёж, шаблон. Описывает, что будет у объекта
- Объект (экземпляр) — конкретная вещь, созданная по чертежу
- Класс — один, объектов — сколько угодно
class Student:                    # класс
    def __init__(self, name):
        self.name = name
student1 = Student("Степан")      # объект
student2 = Student("Аня")         # другой объект

*** __init__ - конструктор
- Вызывается автоматически при создании объекта
- Заполняет объект данными
- Не возвращает ничего через return
- __init__ — два подчёркивания с каждой стороны
def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

*** self - ссылка на объект
- Первый параметр любого метода — всегда self
- При вызове не передаёшь — Python делает это сам
- Через self методы обращаются к своим атрибутам
- student1.introduce() → Student.introduce(student1)
def introduce(self):
    print(f"Привет, я {self.name}")
student1.introduce()   # self = student1
student2.introduce()   # self = student2

*** Атрибуты и методы
- Атрибуты — переменные внутри объекта: self.name, self.done, self.tasks
- Методы — функции внутри класса: def info(self), def add_grade(self, grade)
class Book:
    def __init__(self, title, author, year):
        self.title = title          # атрибут
        self.author = author        # атрибут
        self.year = year            # атрибут
    def info(self):                 # метод
        print(f'"{self.title}" — {self.author}, {self.year}')
    def is_old(self):               # метод
        return self.year < 2000

*** Методы, читающие состояние
- Не меняют объект. Просто читают данные
- info, is_old, average, count, show
def info(self):
    print(f"{self.name}: {self.grades}")
def average(self):
    if len(self.grades) == 0:
        return 0
    return sum(self.grades) / len(self.grades)

*** Методы, меняющие состояние
- Меняют данные внутри объекта. Объект помнит состояние
- mark_done, add_grade, deposit, withdraw, add, remove_song
def add_grade(self, grade):
    self.grades.append(grade)
def mark_done(self):
    self.done = True
def deposit(self, amount):
    self.balance += amount
def withdraw(self, amount):
    self.balance -= amount

*** Связывание объектов (часть 2)
- Объект может содержать список других объектов
- self.tasks = [] — список объектов Todo
- self.songs = [] — список объектов Song
- add — создаёт объект и добавляет в список
- show — перебирает объекты и вызывает их методы
- self.tasks[index - 1].mark_done() — вызов метода конкретного объекта
class TodoList:
    def __init__(self):
        self.tasks = []
    def add(self, title):
        task = Todo(title)          # создаём Todo
        self.tasks.append(task)     # добавляем в список
    def show(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. ", end="")
            task.info()             # вызываем метод Todo
    def mark_done(self, index):
        if index < 1 or index > len(self.tasks):
            print("Нет такого номера.")
            return
        self.tasks[index - 1].mark_done()
Примеры: TodoList → Todo, Playlist → Song, Library → Book

*** Что я написал
- Book — info, is_old
- Todo — mark_done, info
- Student — add_grade, average, info
- BankAccount — deposit, withdraw, info
- TodoList — add, show, mark_done
- Playlist — add_song, show, remove_song, count

*** Ошибки, которые ловил (ООП)
- self.average() = ... — нельзя присвоить вызову метода
- add_garde vs add_grade — опечатка в имени метода
- self.balance = amount — заменяет, а не меняет относительно текущего
- self.tasks[index] vs self.tasks[index - 1] — индексы с 0
- self.author vs self.artist — несовпадение имён атрибутов
- NameError: name 'TodoList' is not defined — объект создаётся внутри класса (отступ)
- :.2f и round() — не делать оба сразу
- Отступы: внутри класса — 4, внутри метода — 8


*** SQL и базы данных
- База данных - организованное хранилище данных
- SQL - язык запросов к БД
- SQLite - встроенная БД в Python

*** Основные команды SQL
- `CREATE TABLE IF NOT EXISTS имя (...)` - создать таблицу
- `INSERT INTO таблица (колонки) VALUES (?, ?)` - добавить данные
- `SELECT * FROM таблица` - выбрать всё
- `conn.commit()` - сохранить изменения
- `conn.close()` - закрыть подключение

*** SQL - фильтрация и сортировка
- `SELECT * FROM таблица WHERE условие` - фильтр
- `SELECT * FROM таблица ORDER BY колонка` - сортировка (возрастание)
- `SELECT * FROM таблица ORDER BY колонка DESC` - сортировка (убывание)
- Операторы: `>`, `<`, `>=`, `<=`, `=`, `!=`, `AND`, `OR`

*** SQL - изменение и удаление
- `UPDATE таблица SET колонка = ? WHERE условие` - изменить (БЕЗ FROM)
- `DELETE FROM таблица WHERE условие` - удалить (С FROM)
- Без WHERE обновятся/удалятся ВСЕ строки!

*** SQL - JOIN и GROUP BY
- `SELECT t1.колонка, t2.колонка FROM t1 JOIN t2 ON t1.поле = t2.поле` - связать таблицы
- `JOIN + GROUP BY` - связать и сгруппировать
- `GROUP BY колонка` - сгруппировать по колонке
- `COUNT(*)` - количество строк
- `SUM(колонка)` - сумма
- `AVG(колонка)` - среднее
- `MAX / MIN(колонка)` - максимум/минимум

*** Работа из Python
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("...")
rows = cursor.fetchall()

*** SQL - правила
- Строки в SQL - в одинарных кавычках: 'Иван'
- Значения - через ? (placeholder): (?, ?)
- = это равно (не ==)
- id INTEGER PRIMARY KEY - автоинкремент (1, 2, 3...)
- conn.commit() - обязателен после INSERT, UPDATE, DELETE
- fetchall() - получить все строки
- fetchone() - одну строку

*** HTTP и API
- HTTP - протокол обмена данными клиент-сервер
- Клиент - запрашивает, сервер - отвечает
- GET - получить, POST - создать, PUT - обновить, DELETE - удалить
- Статус-коды: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error
- JSON - формат данных, похож на словари Python

*** requests
- `import requests`
- `response = requests.get(URL)` - GET-запрос
- `response.status_code` - код (200, 404)
- `response.json()` - преобразовать в словарь/список Python
- `data["key"]` - достать значение по ключу
- `user["address"]["city"]` - вложенные словари
- `for user in users:` - перебор списка словарей

*** Ошибки, которые ловил (SQL)
- Пропущены запятые в CREATE TABLE
- Строки без кавычек в INSERT
- Забыл PRIMARY KEY - id = None
- ORDR вместо ORDER
- UPDATE FROM - лишнее FROM
- quanity вместо quantity - опечатка
- conn.close без скобок
- cursor.fetchall() без цикла/print - данные не выводятся

*** Что я написал (HTTP)
- Запрос поста по id
- Список постов (100)
- Список пользователей (имя, email, телефон, город)

