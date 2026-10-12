import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

posts = response.json()
print(len(posts))

for post in posts[:3]:
    print(post["title"])

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Мой пост", "body": "Привет", "userId": 1}
)
print(response.status_code)

print(response.json())