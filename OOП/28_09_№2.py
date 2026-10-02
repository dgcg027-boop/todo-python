class Todo:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def info(self):
        if self.done == False:
            print(f"[] {self.title}")
        else:
            print(f"[x] {self.title}")

task1 = Todo("Купить хлеб")
task2 = Todo("Помыть посуду")

task1.info()
task1.mark_done()
task1.info()

task2.info()
