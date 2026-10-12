import requests
import json

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
    )
posts = response.json()

with open("posts.json", "w") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

with open("posts.json", "r") as f:
    data = json.load(f)

print("Все заголовки:")
for post in data:
    print(post['title'])