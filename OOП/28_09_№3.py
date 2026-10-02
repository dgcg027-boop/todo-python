class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        else:
           return round(sum(self.grades)/len(self.grades), 2)
    def info(self):
        print(f"{self.name}: оценки {self.grades}, средний балл {self.average()}")


student1 = Student("Степан")
student1.add_grade(5)
student1.add_grade(2)
student1.add_grade(4)
student1.add_grade(5)
student1.info()

student2 = Student("Аня")
student2.info() 