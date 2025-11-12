# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3  gg
b = 4
print(a) #output 3
print(b) #output 4

print(a == b)   # checks for equality                   # False
print(a != b)   # checks if is not equal                # True
print(a > b)    # checks for greater than               # False
print(a < b)    # checks for less than                  # True
print(a >= b)   # checks for greater than or equal to   # False
print(a <= b)   # checks if less than or equal to       # True


#predict the output of the following comparisons:
print(10 > 5)          # True
print(7 == 2 * 3 + 1)  # True
print(8 != 8 )         # False
print(4 <= 2 + 2 )     # True

# Write 3 examples that result in True and 3 that result in False.
print (10 > 3)        # True
print (6 >= 6)        # True
print (9 != 20)       # True 
print (15 >= 28)      # False
print (11 == 7)       # False
print (8 < 2)         # False

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
# # The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
# ask student score
score = int(input(" what is your score?"))
# make this program for all grading spectrums
# if the score is between 90 - 100 -- you got an A
# if the score is between 80 - 89 -- you got a B
# if the score is between 70-79 -- you got a C\
# if between 61 - 69 ,,, you goy a D
# else you failed
if score >= 60:
    print("you passed the test")  
else: 
    print("you didn't pass")

if score >= 90 & score <= 100:
    print (" you got an A!")

elif score >= 80 & score <= 89:
    print (" you got an B!")

elif score >= 70 & score <= 79:
    print(" you got an C")                                                                                                    E
# ask for a password  jkjkkjlkjlkjkjllkjkll;l;;l;l;l;l
#password = input("what is your password?")  bfgb   b
