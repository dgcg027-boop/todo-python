class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f'"{self.title}" — {self.author}, {self.year}')

    def is_old(self):
        return self.year < 2000


book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Гарри Поттер", "Джоан Роулинг", 1997)

book1.info()
print(book1.is_old())

book2.info()
print(book2.is_old())