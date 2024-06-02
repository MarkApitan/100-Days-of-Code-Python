# Instructions
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, 
# you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.


# This is the scoring criteria:
#
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"
# Expected Output
# {'Harry': 'Exceeds Expectations', 'Ron': 'Fail', 'Hermione': 'Exceeds Expectations', 'Draco': 'Fail', 'Neville': 'Fail'}

# Define a dictionary of student scores
student_scores = {
    'Harry': 80,
    'Ron': 65,
    'Hermione': 90,
    'Draco': 70,
    'Neville': 50
}

# Create an empty dictionary to store student grades
student_grades = {}

# Iterate over each key in the student_scores dictionary
for key in student_scores:
    
    # Check the score range and assign the corresponding grade
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        grade = "Outstanding"
    
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        grade = "Exceeds Expectations"
    
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        grade = "Acceptable"
    
    elif student_scores[key] <= 70:
        grade = "Fail"
    
    else:
        grade = "Invalid"

    # Add the student name and grade to the student_grades dictionary
    student_grades[f"{key}"] = grade

# Print the student_grades dictionary
print(student_grades)