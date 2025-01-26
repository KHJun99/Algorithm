Student = []
Base = []

for i in range(1,31):
    Base.append(i)

for i in range(28):
    Student_number = int(input())
    Student.append(Student_number)

for i in range(30):
    if Base[i] not in Student:
        print(Base[i])