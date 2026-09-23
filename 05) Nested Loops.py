# HERE was me learning how nested Loops works
# 18/09/2026

# Nested loop is basicaly having a loop directly inside another loop

# Various Types Of Nested Loops
# 1) For loop with another For loop
# 2) While loop with another While Loop
# 3) For loop with a while loop
# 4) While loop with a For loop 


# Nested For Loop
# This Example prints * in pattern
row = 7
for i in range (1, row + 1):
    for j in range (1, i + 1):
        print ("*", end= " ")
    print (" ")


# Lets see another Nested For loop in action, using a list
aList = ['Excel', 'Dave', 'Jesus']
# now using nested for loop let's put '--' in between each letters
for a in aList:
    for b in a:
        print (b, end='--')
    print ()


# Let's pair two list togther
swallow_List = ["Amala", "Pounded Yam", "Eba", "Semo"]
soup_List = ["Egussi", "Ewedu", "Efo", "Okaro"]
for swallow in swallow_List:
    for soup in soup_List:
        print(swallow, soup)
        print(" ")


colours = ["Green", "Red", "Black", "White"]
cloths = ["Shirt", "Pant", "Jacket", "Round Neck"]

for colour in colours:
    for cloth in cloths:
        print (f"Do you like a {colour} coloured {cloth}?")
    print ()


# Let me try printing patterns again
# Now this is trying to print right angle triangle using "*"
triangle = 10
for triangler in range (1, triangle + 1):
    for i in range (1, triangler + 1):
        print (" ", end="*")
    print (" ")



# Nested "While Loop"
# Let's still try to print the right angle triangle again but now using a while loop
print ("Below is the pattern version using while loop")
triangle = 11
while (triangle > 0):
    triangler = 11
    while (triangler > triangle):
        print ("*", end= " ")
        triangler = triangler - 1
    triangle = triangle - 1
    print (" ")



print ("Here is another test to confrim i understand")
i = 11
while (i > 0):
    j = 11
    while (j > i):
        print ("*", end= " ")
        j = j - 1
    i = i - 1
    print (" ")



# let's try a nested for loop using the append key in python
# here we are going to join two list of numbers together
list1 = [20, 30, 89, 83]
list2 = [48, 99, 83, 10]
result = []
for i in list1:
    for j in list2:
        result.append (i + j)
print (result)


# To multiply two list is also the same step but with our * operator
list1 = [20, 30, 89, 83]
list2 = [48, 99, 83, 10]
result = []
for i in list1:
    for j in list2:
        result.append (i * j)
print (result)

# Let us try to improve the output here using the same list and numbers
list1 = [20, 30, 89, 83]
list2 = [48, 99, 83, 10]
for i in list1:
    for j in list2:
        print (f"{i} * {j} = {i * j} ")
    print ("")



# how about nested loop that has both for and while loop in each other?
# let's print a list muliple times (5X)
classnames = ["Dave", "Glory", "Sam", "Micheal"]
for classname in classnames:
    count = 0
    while (count < 6):
        print (classname, end= " ")
        count = count + 1
    print (" ")



# What if we print patterns like we did earler
# But now we are using numbers and the numbers would even be increasing
print ("Using for loop to print number patterns")
row = 10
for i in range (0, row + 1):
    for j in range (0, i + 1):
        print (j, end= " ")
    print ()


# Let's see break in action again
# Let's asume there is a long list and we only want to print the first 6 integers in the list
numberss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
sum_num = 0
count = 0
for i in numberss:
    sum_num = sum_num + i
    count = count + 1
    if count == 6:
        break
print (f"The sum of the first {count} integers is: {sum_num}")



# Continue Statement
# It's more like telling you to skip a particular iteration if condition is met
# It dosent stop or terminate the whole loop, just jumps 
# Let's see that with printing first 10 integers and Jumping the number 5
print ("This is an example of 'continue' statement and we are to skip the figure 5")
for i in range (10):
    if i == 5:
        continue
    print (i)


# Let's try same thing again for multiple numbers for example
print ("Here we will skip number 3 and 8 using Continue Statement")
for i in range (10):
    if (i == 3 or i == 8):
        continue
    print (i, "is not 3 nor is it 8")


