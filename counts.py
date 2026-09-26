def find_word(text, target):
    words = text.split()
    count = 0
    for word in words:
        if word == target:
            count +=1
    return count

text = input("Введи текст: ")
target = input("Какое слово ищем? ")
result = find_word(text,  target)
print(f"Слово '{target}' встречается {result} раз.")



