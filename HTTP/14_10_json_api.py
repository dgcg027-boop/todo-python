import requests
import json

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
    )
posts = response.json()
with open("api_posts.json", "w") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

with open("api_posts.json", "r") as f:
    data = json.load(f)
for post in data[:3]:
    print(post["title"])