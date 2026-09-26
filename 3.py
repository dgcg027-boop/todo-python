text = input("Введи текст: ")
words = text.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1
print("Одинокие слова:")  
for word, count in counts.items():
    if count == 1:
        print(word)
