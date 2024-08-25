# Write  a program to get the score of the student based on the inputs
# A - 90-100
# B - 89-80
# C - 79-70
# D - 69-60
# E - 59-50

marks = int(input("Enter your marks"))
grade = "F"

if 90 <= marks <= 100:
    grade = "A"
    print(" Your grade is  =", grade)
elif 80 <= marks <= 89:
    grade = "B"
    print(" Your grade is  =", grade)
elif 70 <= marks <= 79:
    grade = "C"
    print(" Your grade is  =", grade)
elif 60 <= marks <= 69:
    grade = "D"
    print(" Your grade is  =", grade)
elif 50 <= marks <= 59:
    grade = "E"
    print(" Your grade is  =", grade)
else:
    grade = " F "
    print("Your grade is =", grade)
