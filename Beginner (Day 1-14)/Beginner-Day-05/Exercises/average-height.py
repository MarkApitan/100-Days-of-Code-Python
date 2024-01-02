# Input a Python list of student heights
total = 0
student_heights = input("What are the students height? ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
  total += student_heights[n]
  students = n + 1
  
average = total/students
average_round = round(average)
print (f"total height = {total}")
print (f"number of students = {students}")
print (f"average height = {average_round}")