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
    # also same as 'sentence = sentence + 1



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






# For Loop
# Can be trying to get numbers in a list like we did above for range
# Also can be used to get values or keys or even both in a dictionary
print ("This for loop is going to print out the numbers i have in a list")
list = [2, 3, 4, 8, 9, 28, 39, 48]
for num in list:
    print (num)
    print (f"Yes, the figure {num} is in thee list")


# let's see dictionary example using 'for loop'
# guess what we can even have a list in a dictionary and i will put that in this
print ("This 'for loop' does pull out what we have in a dictionary")
myDic = {
    'CSC 101': 94,
    'CSC 102': 78,
    'Math 101': 65,
    'PHY 101': 90,
    'CSC 419': 89,
    'Favourite Courses': ['CSC 101', 'PHY 101', 'CSC 419']
}
# Now let's print out only the subjects in the dictionary
for subject in myDic.keys():
    print (f"{subject} is one of the subjects taken")
# How about we try geting only the scores we have in the dictionary?
for scores in myDic.values():
    print (f"Yes, {scores} is one of the scores")
# let's try getting both the subjects and keys right?
for subject, scores in myDic.items():
    print (f"In {subject} your score is: {scores}")



# Nested For Loop
# More like nested If statement we did last weeek, here we will have a "for loop" inside another
print ("AN example of 'Nested For Loop'")
print ("This Will pair two diffrent list together")
swallow = ['Eba', 'Amala', 'Semo', 'Pounded Yam']
soup = ['Egussi', 'Ewedu', 'Efo', 'Okro']
# Now let's pair swallow with each stew giving customers what we can offer in a local resurant
for swa in swallow:
    for sou in soup:
        print (f"Yes, you can order {swa} with {sou}")



# CONTINUE STATEMENT
# Basicaly skips the current condition of the iteration
# For example let us print frist 5 integers and we skip number 3
for int in range(5):
    if int == 3:
        print ("Move to the next")
        continue
    print (int)



# Let's try this continue statement for a real life example
# A sum we have 100 cups of cake to sell
# So we have to skip others that request us to deliver more than 100
# But we still need to sell other remaining that is less than 100

cost = 5.97
cupOFcake = 100
# while we still have more than 0 cup cakes let's take order
while cupOFcake > 0:
    order = float(input("How Many Cups OF Cakes Are You Buying today? "))
# if we don't have up to the requested cup of cakes let's skip and take another order
    if order > cupOFcake:
        print ("Sorry, your order is above what's left.")
        continue
    print (f"You ordered for {order} Cups of Cake and the total is: {order * cost}")
    cupOFcake = cupOFcake - order
print ("Sorry, No Cakes left. We love you at Exceled Cakes")



# Quicly a for loop to print integers withing a particular range
print ("Below are the integers between 3 and 10")
num = 10
for i in range (3, num):
    print (i)


# let's again use for loop to multiply a list and a particular number
list1 = [2, 4, 6, 8, 10]
by = 5
for i in list1:
    print (f"{i} multiply by {by} is: ", i * by) 

# Another more explanatory way
print (" ")
list1 = [2, 4, 6, 8, 10]
by = 5
for i in list1:
    mul = i * by
    print (f"{i} multiply by {by} is: {mul}")



# While Loop
print ("Here is using while loop to count from 0 to 20")
count = 0
while (count < 21):
    print (f"Now we are at count: {count}")
    count = count + 1









# What if we want for first odd integers?
# num = int(input("How many frist odd integers do you want to add? "))
# total = 0
# for i in range (2, num + 2):
#     total += i
# print (f"The addition of frist {num} odd integers is {total}")