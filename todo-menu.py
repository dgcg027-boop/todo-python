def load_todos():
    try:
        with open("todos.txt", "r") as f:
            lines = f.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open("todos.txt", "w") as f:
        for task in todos:
            f.write(task + "\n")        

def show_todos(todos):
    if len(todos) == 0:
        print("Список пуст")
        return
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

def add_todo(todos):
    task = input("Новое дело: ")
    todos.append(task)
    save_todos(todos)
    print(f"Добавлено: {task}")

def remove_todo(todos):
    show_todos(todos)
    if len(todos) == 0: 
        return
    try:
        n = int(input("Какой номер удалить? "))
    except ValueError:
        print("Это не число!")
        return

    if n < 1 or n > len(todos):
        print("Нет такого номера.")
        return
    removed = todos.pop(n-1)
    save_todos(todos)
    print(f"{removed} - удалено.")

def main():
    todos = load_todos()
    while True:
        print("\n1. Показать 2. Добавить 3. Удалить 4. Выход")
        choice = input("Что делаем? ")

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            remove_todo(todos)
        elif choice == "4":
            print("Пока")
            break
        else:
            print("Нет такого пункта.")
main()

