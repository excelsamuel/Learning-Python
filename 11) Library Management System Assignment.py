# 01/10/2026
# Unit 5 Assinment: Library Management System

# Question 1:
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

#Adding two more books one by one
books.append("Rich Dad Poor Dad")
books.append("The Art of War")

#Removing our damaged book "Moby Dick" from the list
books.remove("Moby Dick")

#Arrange the books alphabetically
books.sort()

#Let's Print out the final list
print("The list of the currently available books are:")
for book in books:
    print(book)



# Question 2:

print()
print("Now we are working with a Tuple")

borrower = ("John Doe", "B1023", "2025-10-15")

print("Original borrower's details are:", borrower)

#Let's try to modify one of the elements
try: #try is used to catch the error and not break my program totally
    borrower[2] = "2026-01-15"
except TypeError as error:
    print("Modification result:", error)

#Checking for the length of the tuple
print("The lenght of data in the field is:", len(borrower))

#Let's see each element by iterating through the tuple
print("Borrower details is still:")
for detail in borrower:
    print(detail)



# Question 3:
print()
# Let's pack a Tuple
book_info = ("The Art of War", "Sun Tzu", "500 BC", "Thomas Cleary")

#Now let's unpack the Tuple
title, author, publication_year, translator = book_info

print("The Book information below:")
print("Title:", title)
print("Author:", author)
print("Publication Year:", publication_year)
print("Translator:", translator)



# Question 4:
# Let's create a list of borrowed books for a week and we can modify it as instructed
print()
print("Now we are working with a List again:")

borrowed_books = [23, 19, 31, 27, 22, 30, 25]

# Using slicing to extract weeks 2 to 5
weeks_2_to_5 = borrowed_books[1:5]

#Next we will replace week 1 result with 20
borrowed_books[0] = 20

print("This is the updated weekly borrowing statistics:", borrowed_books)
print("Here is also our borrowing statistics for weeks 2 to 5:", weeks_2_to_5)
