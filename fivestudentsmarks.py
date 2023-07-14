avg =[]
stdx =[]
for i in range(0,5):
    student =[]
    sumz =0
    for j in range(0,5):
        marks = int(input(f"Enter the marks of students {i+1}:"))
        student.append(marks)
        sumz += marks
    stdx.append(student)
    avg.append(sumz/5)
print(stdx)
print(avg)
