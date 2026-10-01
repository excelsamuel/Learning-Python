# 01/10/2026

# Types of collectors in python
#  List [ ]
#  Set { }
#  Tuple ( )
# This collection is a single "Variable" used to store multiple values


# Let's start with a List
# List [ ]
# List is ordered, changeable and very okay to have duplicated values
fruits = ["Apple", "Grape", "Orange", "Coconut"]
# we can do a lot with this fruits list

#print(dir(fruits))   #To check the characteristicts of the list
#print(help(fruits))  #To see how we can use the list
print(len(fruits))   #This returns the length of the list
# ps: "help", "len", "dir" can be used even in set and tuples not only in list

# Others particular to list are:
print("This is the first three items in the list:", fruits[0:3])
print("This is the second items in the list:", fruits[1])
# We can decide to change an item in the list
fruits[0] = "pineapple"
print("This is the updated list", fruits) #You will see in the output that apple is replaced with pineapple
fruits.append("Mango") #append is to add new object to the list
print("Adding more fruits to the list", fruits)
fruits.remove("Grape")
print("Grape is removed because user dont like it, new list is:", fruits)
fruits.insert(1, "Watermellon") #We inserting at a specific location and not replacing
print("User jsut added Watermellon:", fruits)
fruits.sort() #The fruit is sorted alphabetically
print("The Fruit is now arranged orderly:", fruits)
fruits.reverse()
print("Now we reverse the arrangement:", fruits)
print(fruits.clear)



# SET { }
# Set is actually unordered and immutable but you can Add or remome from it
# Also set do not permit for duplicates 
# Let's do some basics with set using our fruits example
print()
print("We are now working with SET { }")
fruits = {"Apple", "Grape", "Orange", "Coconut"}
fruits.add("Pineapple")
print("We have added pineapple to this list:", fruits)
fruits.remove("Orange")
print("Orange is removed from the list by user:", fruits)
print("The user used the pop keyword which returns a random fruit from the set: ", fruits.pop())
print("The fruits set is cleard and returns:", fruits.clear()) 



# Tuple ( )
# Tuple on the other hand are ordered and unchangable also it permit for duplicates of elements in it
# Tuple is much more faster to work with
# we can only do majorly "index" and "count" in a Tuple
# Again let's see how it works with our fruit example
print ()
print("Now we working with a TUPLE ( )")
fruits = ("Apple", "Grape", "Orange", "Grape", "Mango", "Mango", "Grape", "Coconut")
print("In the tuple Apple is at index: ", fruits.index("Apple"))
print(f"We have {fruits.count("Mango")} numbers of mango in our tuple")
print(f"We have {fruits.count("Grape")} numbers of Grape in our Tuple")



# Immutable Vs Mutable
# The english word is pretty explanatory. One can be changed and one cant be changed

# Mutable Examples:
#  1) Sets
#  2) Lists
#  3) Dictionaries

# Immutable Examples:
#  1) Tuple
#  2) Sring
#  3) Frozen Set ({1, 2, 3})

# But also in python you can have a list inside a tuple which makes the list in the Tuple changeable and not the whole tuple just the list in it
#  something like:
#  (1, 2, ["a", "b", "c", "d"], 13)
# Inside the index 2, we can be change somethings because it's a list



# Unpacking a Tuple in Python
# Packing is assigning values to a tuple
# While Unpacking is extractinng values from a tuple and putting them in variables
# Let's see this example to see how it works 
print()
print("We are now working with unpacking variables right now")
cars = ("Mercedes", "BMW", "Toyotal")
car1, car2, car3 = cars
print(car1, "is the frist car") 
print(car2, "Is the seond car name")
print(car3, "Is the thrid car in the tuple")


# The use of Asterisk in unpacking of tuple
# How about when we have less variable names compared to the long list of element in the tuple
# This is where (*) comes in...
# Let's see an example below
print()
print("Here we unpack a tuple with the use of Asterisk in action")
cars = ("Mercedes", "BMW", "Toyotal", "Audi", "Ford", "Ferari")
car1, car2, *car3 = cars
print(car1, "is the frist car") 
print(car2, "Is the seond car name")
print(car3, "Those are the other cars available")
# As you can see we have 6 elements in our tuple but only 3 variable names
# The (*) is used before the last variable name so the last variable can unpack all the remaining elements


# it's also the same if the (*) is used with any other variable name even if it's not the last one
# If the asterik is used with a variable other than the last variable then the values are assigned until the value left matches the value left 
# Let's see this in action
print()
print("Now let's unpack a variable with (*) but not the last variable name carrying the asterisk")
cars = ("Mercedes", "BMW", "Toyotal", "Audi", "Ford", "Ferari")
car1, *car2, car3 = cars
print(car1, "is the frist car") 
print(car2, "are also cars available")
print(car3, "is the last car in the tuple")

