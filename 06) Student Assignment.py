
# Questions 1:
students = ["Alice", "Ben", "Chloe", "David"]

for student_name in students:
    print(student_name)

# Question 2:
grades = []

while True:
    grade = input("Enter a student's grade or type 'done' to end: ")

    if grade.lower() == "done":
        break
    grades.append(float(grade))
print("This are the list of Grades entered:", grades)


# Question 3:
# Let's see both "break" and "continue" statements in action
grades = []

while True:
    grade = input("Enter a grade or type 'done' to end this: ")
# let's use "break" to exit the loop when the user types 'done'
    if grade.lower() == "done":
        break

    grade = float(grade)
# here let's  use "continue" to take care of invalid grades inputed
    if grade < 0 or grade > 100:
        print("Invalid grade. Kindly input a grade between 0 and 100.")
        continue
# The loop will only skip the invalid input and continue with the collection
    grades.append(grade)
print("The Valid Inputed grades are:", grades)


# Question 4: Nested Loops
# Let's see how nested loops works in action
# Here we have two classes, each with a list of students. We will use nested loop to print out all possible pairs of students from the two classes.
class1 = ["Alice", "Ben"]
class2 = ["Chloe", "David"]

for student1 in class1:
    for student2 in class2:
        print(f"{student1} and {student2} are in Separate classes.")
# Print a blank line for better readability
    print()  

# Another example of Nested Loops
# Let's say we have posible grades for the students
class1_names = ["Chloe", "David", "Alice", "Ben"]
class2_grades = [80, 92, 60, 20]

for name in class1_names:
    for grade in class2_grades:
        print(f"{grade} might be {name}'s grade.")
    print() 