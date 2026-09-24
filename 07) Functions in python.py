# In this note pad i am going to learrn how to create and use my own "Functions" 
# Over the time i have only known how to use general functions like "print", "round" and co
# Important key here is the "def" key
# 24/09/2026

# Creating my own fuction so that when i call greet_me it says Hi and even ask about someone
def greet_me ():
    print ("Hello, Excel")
    print (" How's Dave doing?")

# now let me call the function i just created above
greet_me ()


# Arguments
# Quickly let's put in arguments and perameters into our example above
# More like making it more personal
def greet_mee (first_name, last_name): #this is the parameters in the brackets
    print (f"Hello {first_name} {last_name}")
    print ("How are you doing today?")

greet_mee ("Excel", "Dave") #this are the arguments here that's enclosed
greet_mee ("Ray", "Silver")



# Types of function
# 1) The one that perform a task
# 2) The one that returns a value after calculation
# Wehave example of the first one at the top already, let's see the second one in action
def greet_meee (name):
    return (f"Hi {name}")

message = greet_meee ("Dave")
# now that we even decleared the function as a variable we can use it how we like
# we can call it to pint or even used to open a new file, it will be available to use much better than only the plain print that performs a print task
print ("Below is the message in our function that we used return for instead of print")
print (message)


# Let's try again with increasing a perticular number
def increment (number, by):
    return (number + by)

result_by = increment (3, 1)
print (result_by)


# now what i just did above let's simplify the code
def increment (number, by):
    return (number + by)

# now we can join those two lince in the other code together to give  one and will still do the same thing
print (increment (3, 1))


# Now still on that same example let us make the code more  readable
# So if someone else see the code they can easily tell what we are doing
def increment (number, by):
    return (number + by)

print (increment (number = 3, by = 1))
# here you can easily tell which parameter we are pairing with an argument
# This is supper useful when dealing with a lot of arguments


#let me take for example i want by to carry a value
# and that value is used when i don't give the argument 
# Yes using the same example
def increment (name, by = 1):
    return (name + by)

print ("This uses the defult by, result is:", increment(2))
print ("This uses a new by value and result is:", increment(2, 3))
# so with that we can optionaly use the defult or even not use it and have a new value for it during our argumment
# But there is a rule, all the optional parameters must only come after the required perameters
# you can't write """ def increment (name, by = 1, number)"""
# You can only write that as """def increment (name, number, by = 1)"""


# *arg
# What if we don't know the numbers of arguments that's coming later
# But we still need to declear our perameters regardless
# This is where something like this shows up: *args, *number 
def multiply (*numbers):
    total = 1
    for number in numbers:
        total = total * number
        # or total *= number
    return (total)

print (multiply (1, 2, 3, 4, 5))
# as you can see here we multiply our argument tuple using a for loop
# while we use the *numbers we can decide to use any lenght of argument


# **arg
# The double asterisk in parameter help us add multiple keys during our arguments
# Those key and values in our argument in python are then stored as dictionary
# This example let us try to save details of one or two users
def user_details (**user):
    print (user)


user_details (id = "2891XJ", name = "Dave", age = 22, location = "London", Sex = "Male")
user_details (id = "8991LM", name = "Samuel", age = 24, location = "Canada", Sex = "Male")
# as you can see the output of the print we used will give all in a dictionary output

# Okay let's say we want to get only the name from the dectionary
# That can happen by just adjusting what we put inside the print
# Using the same example
def user_details (**user):
    print (user["name"])
    print (user["location"])


user_details(id="2891XJ", name="Dave", age=22, location="London", Sex="Male")
user_details(id="8991LM", name="Samuel", age=24, location="Canada", Sex="Male")



# Exercise
# Le's solve a fizz_buzz
# The rules are... if the number is divisible by 3 it will return the string "fizz"
# ...if the number inputed is divisible by 5 it will return "buzz" 
# ...if the number is divisible by both 5 and 3 it will return fizzbuzz
# ...if the number is  not divisible by anyone it will return the number itself

def fizz_buzz (input):
    if (input % 3 == 0) and (input % 5 != 0):
        print ("fizz")
    elif (input % 5 == 0) and (input % 3 != 0):
        print ("buzz")
    elif (input % 3 == 0) and (input % 5 == 0):
        print ("fizzbuzz")
    else:
        print (input)


print(fizz_buzz(7))


# It was correct, it worked but we can do a little clean up
# Another notice from the correction is i was using the "print" instead of "return" as we might need to work on the result later
# So another clearner version
def fizz_buzz (input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if (input % 3 == 0):
        return "fizz"
    if (input % 5 ==0):
        return "buzz"
    return input


print (fizz_buzz(7))
# Do you know things that changed?
# the else if "elif" is not that needed as if the condition in an if is not true it automaticaly moves to the next thing
# Also the retun key instead of print that limits what we can do with the result
# Another thing is that the one that checks if 3 and 5 is divisible is moved to the top as important
# At the end of the day the two is correct but one is much more clean and less line of codes 



# LAMBDA 
# Lambda are small anonymous function for one time use
# They do help keep the name space clean and naming them is not needed as it's used only once
# lambda syntax:
#       map (lambda X: X * 2, numbers)
# you will likely see lambda in use with higher functions like 'sort()', 'map()', 'reduce()', 'filter()'

# let's use lamba for basic function as example first
double = lambda X: X * 2

print (double(2))

# still on basic function
# Let's try to add two numbers together
add = lambda X, Y: X + Y

print (add (2, 5))

# let me use the same lambda to find if and integer is greater than the other
diffrence_max = lambda X, Y: X if X > Y else Y 

print ("The",diffrence_max (9, 6))

# Next let's do the opposite and get the minimum number between two variables
