with open("hello.txt", "w") as f:
    f.write("Привет, файл")
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)