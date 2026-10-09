# 09/10/2026
# SETS and DICTIONAIRES

# SETS { }
# In set we have primarily four operations like:
#  Union: '|'    This will give all unique elements in the available sets
#  Intersection: '&'   This will return the common elements in the declared sets
#  Diffrence: '-'     This will present elements that are not common in the list of available sets
# Symmetric Diffrence: '^'   This prints all other elements that are not common in the diffrent sets
# Let's see example


even = {0, 2, 4, 6, 8, 10}
normal = {1, 2, 3, 4, 5, 6}

print("The Union of the two sets is: ", even | normal)
print("The Intersection of the two sets is: ", even & normal)
print("The Diffrence of the two sets is: ", even - normal)
print("The Symmetric Diffrence of the two sets is: ", even ^ normal)



# DICTIONAIRES  {Key : Value}
# They contains collection of {key:value} pairs that are ordered and changable but do not permits duplicates
# Let's see an example using countries and their capitals

capitals = {
    "USA" : "Washington, D.C.",
    "Canada" : "Ottawa",
    "Mexico" : "Mexico City",
    "Brazil" : "Brasilia",
    "United Kingdom" : "London",
    "France" : "Paris",
    "Germany" : "Berlin"
}

# now we have our dictionary above and we can do alot with it like:
print(capitals.get("USA")) #This will return the respective value of the key "USA"
capitals.update({"Japan" : "Tokyo"}) #this .update can help add new key and value to our dictionary
print (capitals)

capitals.update({"USA" : "New York City"}) #You can also overried, like change the value a key carries
print(capitals)

capitals.pop("Brazil") #The pop removes a key and the value from the dictionary
print(capitals)

capitals.popitem() #This 'popitem()' i just used is to remove the last item in the dictionary without using the key
print(capitals)

# capitals.clear() #pretty straightforward, it's use to clear the dictionary's data
# print(capitals)

print(capitals.keys()) #This gives us the keys in the dictionary

# We can even iterate the keys so it comes out as a list
for key in capitals.keys():
    print(key)

# Also the same goes with geting the values in the dictionary
print(capitals.values())

# The same thing let's iterate through the values
for value in capitals.values():
    print(value)

# What if we want to iterate through the whole dictionary's keys and values togther?
for key, value in capitals.items():
    print(f"The capital of {key} is called {value}")

print(capitals.items()) #To give the whole dictionary's items
