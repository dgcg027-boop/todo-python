class Todo:
    def __init__(self, title):
        self.title = title
        self.done = False
    def mark_done(self):
        self.done = True
    def info(self):
        if self.done:
            print(f"[x] {self.title}")
        else:
            print(f"[ ] {self.title}")

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        task = Todo(title)
        self.tasks.append(task)

    def show(self):
        if len(self.tasks) == 0:
            print("Список пуст")
            return
        for i, task in enumerate(self.tasks, start =  1):
            print(f"{i}. ", end="")
            task.info()
    def mark_done(self, index):
        if index < 1 or index > len(self.tasks):
            print("Нет такого номера")
            return
        self.tasks[index - 1].mark_done()


todo_list = TodoList()

todo_list.add("Купить хлеб")
todo_list.add("Помыть посуду")
todo_list.add("Сделать уроки")

todo_list.show()
todo_list.mark_done(2)
todo_list.show()
todo_list.mark_done(99)   # Нет такого номера.
    

