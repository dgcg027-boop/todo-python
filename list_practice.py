todos = []
for i in range(3):
    task = input("Дело:")
    todos.append(task)
while len(todos) > 0:
    print("Список дел:")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")
    done = input("Что выполнено? ")
    if done == "хватит":
        print("Выходим. Осталось дел:", len(todos))
        break
    if done in todos:
        todos.remove(done)
        print(f"{done} — удалено.")
    else:
        print("Такого дела нет.")
if len(todos) == 0:
    print("Всё выполнено!")

