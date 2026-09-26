text = input("Введите текст из трёх слов: ")
words = text.split()

with open("text.txt", "w") as f:
    for word in words:
        f.write(word + "\n")
with open("text.txt", "r") as f:
    content = f.read()
print(content)