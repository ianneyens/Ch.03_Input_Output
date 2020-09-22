'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

print()
print("Welcome to the grade calculator")
print()
sem = int(input("What is your Semester Grade:"))
print()
final = int(input("What is your Final Exam Grade:"))
print()
exam = float(input("What is your Final Exam Worth (decimal):"))
sem_w = 1-exam
over = (sem*sem_w)+(final*exam)
print()
print("Your final grade will be", over)
