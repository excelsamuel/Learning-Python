print ("Day 5 with Python Learning. 12/09/2026")
#Conditional Statement In Python
# we have: 
# 1) if Statement
# 2) if else Statement
# 3) elif Statement
# 4) Nested if Statement
# 5) Nested if else Statement


print ("Welcome To Conditional Statement In Python Class")

# Let's demostrate how the "if statement work"
# It returns true if the condidtion is met
print ("This is section shows how if statement works")
grade = int(input("My Grade is: "))
if grade >= 50:
    print ("You have passed!!!")


# if else statement
# Next is to see how to use the "if else statement"
print ("Next section is how if else statement works")
grade = int(input("My Grade is: "))
if grade >= 50:
    print ("Congratulations you passed!!!")
else:
    print ("Oh You Failed")



#Next is how Elif Statement works 
# This example i will try to cater for somone that input value above 100
print ("Below shows how elif statement works") 
grade = int(input("My Grade is: "))
if grade >= 50 and grade < 100:
    print ("Congratulations, You Passed!")
elif grade < 50:
    print ("Sorry you failed")
else:
    print ("Your inputed grade is invalid, you inputed: ", grade)

# 
# Another example still under the elif statement
print ("This Section tells you the grade of your score either A, B, C, D, or F")
score = int(input("My Math Test Score is: "))
if score >=70 and score <= 100:
    print ("Congratulations, you passed with A Grade")
elif score >= 60 and score <= 69:
    print ("Congratulations, you passed with B Grade")
elif score >= 50 and score <= 59:
    print ("Congratulations, you passed with C Grade")
elif score >= 45 and score <= 49:
    print ("Congratulations, you passed with D Grade")
elif score >= 40 and score <= 44:
    print ("Congratulations, you passed with E Grade")
elif score < 40 and score >= 0:
    print ("Sadly, you failed with F Grade")
else:
    print ("Your score is not valid, your inputed score was: ", score)

# Else If Satement for a Loop example
# Another Example using the "For Loop" and "in range" still under else if statement i.e "Elif Statement"
print ("This example checks what X could be in a range of number 0-9")
for X in range(10):
    if X <= 3:
        print (X, "is less than or equal to 3")
    elif X >= 5:
        print (X, "is above or equal to 5")
    else:
        print (X, "must be equal to 4")



# Let's check for "Nested if statement"
# for this nexted if statement, we have if statement inside of each other
print ("Example for a Nested if Statement")
num = int(input("Input your prefered number: "))
if num <= 500:
    print (num, "is less than 500")
    if num <= 300:
        print (num," is also less than 300")
else:
    print (num, "Is definatly above 500")



# Here let's check for how "Nested if else Statement works"
# In this statement there are multiple if and else statemenet in each other
print ("Example for a Nested if else statement below")
A = int(input("Reply with your preffered number: "))
if A < 50:
    if A % 3 == 0:
        print (A, " is less than 50 and Divisible by 3")
    else:
        print (A, " is is less than 50 but not Divisible by 3")
else:
    print (A, " is above 50")
    