# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Get the student's score as input
score = float(input("Enter the student's score: "))
#Determine the letter grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the result
print("The letter grade is:", grade)