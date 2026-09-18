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
        print (a, end= '--')
    print ()


# Let's pair two list togther
swallow_List = ("Amala", "Pounded Yam", "Eba", "Semo")
soup_List = ("Egussi", "Ewedu", "Efo", "Okaro")
for swallow in swallow_List:
    for soup in soup_List:
        print(swallow_List, soup_List)
        print(" ")


