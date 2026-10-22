import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
data = response.json()
print(data["title"])

#Задача 2
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 2}
    )
posts = response.json()
print(len(posts))

#Задача 3
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()
print(data["name"])
print(data["email"])