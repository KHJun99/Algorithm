grade1 = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade2 = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]

course_credit = 0
total = 0

for i in range(20):
    A, B, C = input().split()
    B = float(B)

    if C != "P":
        course_credit += B
        total += B * grade1[grade2.index(C)]


average = "{:.6f}".format(total / course_credit)
print(average)
