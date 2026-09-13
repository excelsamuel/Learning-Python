# 07/09/2026 - 13/09/2026
# This is @excelsamuel 's note
# Learning the basic Data Types in python and how they works

x = 1000
y = "Excel learning Python"
z = 25.5

# now let us check those Data Type using type()
print (type(x))
print (type(y))
print (type (z))

# the output will auto dectect and tell us the data type of each above and should give something like...
# <class 'int'>
# <class 'str'> 
# <class 'float'>


a = 10
print ("The type of a is", type(a))

b = 10.27
print ("The type of b is", type(b) )

c = 4+5j
print ("The type of c is", type(c))
print ("C is a complex value", isinstance(4+5j, complex))


# Trying to understand list and + , * operations here
L1 = [10, "Hello", "World", 30, 40]
print (type(L1))

L2 = [20, "Hello", 88.8]
print (type(L2))

# Now let's print them out
print (L1)
print (L2)

# Let's do the + Function of the two of them
print (L1+L2)

#Let's try out the * function
print (L1 * 4)

# let's say i only want the list of value after the 3 value in L1
print (L1[3:])
print (L2[0:2])
# the above are the same


# Dictionary
# Now let's work and see how Dictionary works in python
Dic = {101:'Excel', 102:'Samuel', 103: 'Tayos', 104:'Dave'}
# Let's print the whole Dictionary
print(Dic)
# Let's print one records
print ("Your Second Record Is:" +Dic[102])
print ("Your Third Record Is:" +Dic[103])
# What if we want to print Dictionary's Keys and Values diffrently?
print (Dic.keys())
print (Dic.values())



# BOOLEAN
# Next let's test for Boolen and see the False and True thing
# In Boolean 0 is false and anyother whole number is true
print  ("This is the BOOLEAN Section")
M = bool(1)
N = bool(0)
# let's know which is true or false
print (M)
print (N)
# Now let's see the data type of them
print (type(M))
print (type(N))



# SET
# Next data type we working with is set
#     SET Data are unsorted data and also permits editing a given set of data
print ("Bellow shows How a set works")
emp_set =()
set_data = {'Exceled',28,'Daved'}
print (set_data)
# Now let's try adding to the data
set_data.add (23)
set_data.add ('Mercy')
# Let's print again to see the diffrence
print (set_data)
# let's try to remove something from the data set
set_data.remove(28)
# let's print again to see the diffrence
print(set_data)



# Type of conversion
# we have two which are "Implicit and Explicit Type Conversion"

# Let's see how Implicit Type Of Conversion works
# In python it automatically convert one data type to another without the assistance of the User
# For Example
print("Implicit Type Of Conversion")
num_int =25
num_float = 25.5
new_num = num_int + num_float
print ("The Data Type Of num_int is:", type(num_int))
print ("The Data Type Of num_float is:", type(num_float))
print ("The Value Of new_num is:", new_num)
print ("The Data Type of new_num is:", type(new_num))

# Explicit Type Conversion
# Here the user is involved and using something like Type casting
# It involves the use of some pre-defined functions like "int()" "float()" "str()" etc
# For Example, we gonna convert string to integer here
print ("This is For Explicite Type of Data Conversion")
E = 467
F = "234"
print ("The Data Type of E is:", type(E))
print ("The Data Type of F is:", type(F))
# Now let's type cast F telling it it's an Integer
F = int(F)
print ("After Type Casting F type is now:", type(F))
sum = E + F
print ("Sum of E and F is:", sum)
# now let's see the data type of sum
print ("Data Type of Sum is:", type(sum))


# OPERATORS
# We have various Operators in Python 
# Arithmetic Operators
# Relational Operators
# Assignment Operators 
# Unary Operators 
# Bitwise Operators
# Logical Operators
# Membership Operators
# Identity Operators


# Let's see Arithmetic Operators in Action
print("This Is Arithmetric Operators In Action")
C = 4
D = 2
# We already knows how Addition +, Miltiplication *, and Subtractions works
DivisionOfCD = C/D
print ("C divided by D is:", DivisionOfCD)
ModulusOfCD = C % D
print ("The Modulus of C and D is:", ModulusOfCD)
SquareOfCbyD = C ** D
print ("The Squre Of C by D is:", SquareOfCbyD)
# Floor Division
FloorDivision = C // D
print ("The Floor Division Of C by D is:", FloorDivision)


# Next is seeing Assignment Operators in Action
print ("This shows how Assignment Operators Works")
X = 5
print ("X is =", X)
X += 5
print ("X + 5 =", X)
X -= 5
print ("X - 5 =", X)
X *= 5
print ("X * 5 =", X)
X /= 5
print ("X / 5 =", X)
X %= 5
print ("X % 5 =", X)
# Let's declear X to be 5 again as the previous X is already Zero
print ("Here X is redecleared to be equal to 5")
X = 5
X **= 5
print ("X ** 5 =", X)
X //= 5
print ("X // 5 =", X)

