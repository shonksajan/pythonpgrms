student =[]
for i in range(0,5):
    marks = int(input("Enter the marks:"))
    student.append(marks)
sum = sum(student)
print(len(student))
print("Average marks of student"+str(sum/5))