class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def info(self):
        print(f'"{self.title}" - {self.author}')

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    def show(self):
        if len(self.books) == 0:
            print("Библиотека пуста")
            return
        for i, book in enumerate(self.books, start = 1):
            print(f"{i}. ", end="")
            book.info()
    def find_by_author(self, author):
        found = []
        for book in self.books:
            if book.author == author:
                found.append(book)
        return found
    def show_found(self, author):
        found = self.find_by_author(author)
        if len(found) == 0:
            print(f"Книг автора {author} не найдено")
            return
        print(f"Книги автора {author}: ")
        for book in found:
            book.info()

library = Library("Городская")
library.add_book("Война и мир", "Лев Толстой")
library.add_book("Анна Каренина", "Лев Толстой")
library.add_book("Преступление и наказание", "Фёдор Достоевский")

library.show()
library.show_found("Лев Толстой")
library.show_found("Пушкин")