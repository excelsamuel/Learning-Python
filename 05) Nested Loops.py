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