# Input a list of student scores
student_scores = input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highscore = 0
for scores in student_scores:
  if highscore < scores:
    highscore = scores

print (f"The highest score in the class is: {highscore}")