import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json = {'title': 'Мой пост', 'body': 'Привет, мир', 'userId': 1}
    )
print(response.status_code)
print(response.json())

#Задача 2

import requests

response1 = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json = {'id': 1, 'title': 'Обновлённый', 'body': 'Новый текст', 'userId': 1}
    )
print(response1.status_code)
print(response1.json())

#Задача 3

import requests

response2 = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response2.status_code)
print(response2.json())