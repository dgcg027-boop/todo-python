name = input("Введи имя студента: ").lower()
marks = []
for i in range(3):   
    mark = int(input("Введи оценкe: "))
    marks.append(mark)
mid = round(sum(marks)/len(marks), 2)
with open("student.txt", "w") as f:
    f.write(f"Студент: {name}\n")
    f.write(f"Средний балл: {mid}\n")
with open("student.txt", "r") as f:
    content = f.read()
print(content)
 