# Iterative Satements
# 15/09/2026

# There are some statements that require us to repeat for a multiple number of time or even forever
# This is where iterative Statement comes in, we call them loops also
# The Two Types are
#   1) For Loop
#   2) While Loop

# FOR LOOP
# Let's say i can be from 1 to 9
print ("Checking how for loops works here")
for i in range(10):
    print (f"Yes, i can be {i}")

# What if we want to say i can be from maybeb 2 to 10
# Side note: First index will always be 0, it starts from 0 not 1
print ("This is the range between two numbers")
for i in range(2,11):
    print (f"Yes, i can be {i}")

# what if i want to print I LOVE YOU 10 times using for loop?
for i in range (10):
    print (i, ". I LOVE YOU!")

# Let me use the for loop to know the sum of the first 10 integers
total = 0
for i in range (1, 10 + 1):
    total += i
    print (total)

# What if we want to do sum of the first integers specified by the user?
num = int(input("Enter the number of the first integers you want to print: "))
total = 0
for i in range (1, num + 1):
    total += i
print (total)



# WHILE LOOP
# The secon type of iterative statement
# if the while is True it goes ahead to execute the body of while
# Then comes back again to check if true goes ahead to repeat the process
# Until the while statement becomes false
print("LET'S SEE WHILE LOOPS IN ACTION")
# let's write the statement "I am enjoying learning Python" 10 times
sentence = 0
while sentence < 10:
    print ("I AM ENJOYING LEARNING PYTHON")
    sentence += 1



#  BREAK STATEMENT
# In Iteration break statement is used to stop the normal flow of the repetition
# It can be used in both for loop and while loop
print ("Let's use Break Statement in this 'for loop'")
# let's say the for loop program below is to print first 10 integers
# And we want it to stop at 6th integer
# num = 0
for num in range (10):
    print (num)
    if num == 7:
        break
print ("The program was broken at: ", num)

































# What if we want for first odd integers?
# num = int(input("How many frist odd integers do you want to add? "))
# total = 0
# for i in range (2, num + 2):
#     total += i
# print (f"The addition of frist {num} odd integers is {total}")