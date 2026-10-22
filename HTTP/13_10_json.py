import requests
import json

person = {"name": "Степан", "age": 21, "city": "Москва"}
with open("person.json", "w") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)
with open("person.json", "r") as f:
    data = json.load(f)
    print(data["name"])
    print(data["city"])

#Задача 2
import requests
import json

books = [
    {"title": "Война и мир", "author": "Толстой", "year": 1869},
    {"title": "1984", "author": "Оруэлл", "year": 1949}
]
with open ("books.json", "w") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)
with open("books.json", "r") as f:
    data = json.load(f)
for item in data:
    print(item["title"])
