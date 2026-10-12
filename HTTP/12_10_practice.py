import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/5")
users = response.json()


print(users["title"])
print(users["userId"])

#задача 2
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1}
)
posts = response.json()
print(f"Комментариев: {len(posts)}")

for post in posts:
    print(post['email'])

#Задача 3
import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Тест", "body": "Текст", "userId": 2}
)
print(response.status_code)

print(response.json())