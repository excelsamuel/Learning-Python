# 23/10/2026

# This is a Smart Personal Assistant that can perform various tasks such as calculating square roots and providing motivational quotes.

# Question 1
# Example 1
import math as m

number = 81
result = m.sqrt(number)

print(f"The square root of {number} is {result}")


# Example 2:
# This question asks the assistant to provide a random motivational quote.
import random as rd

quotes = [
    "Small steps lead to big achievements.",
    "Consistency is more important than perfection.",
    "Every day is another opportunity to learn.",
    "Believe in yourself and all that you are."
]

print(rd.choice(quotes))


# Example 3
# This question asks the assistant to provide the current date and time.
import datetime as dt

today = dt.datetime.now()
print(f"Current date and time: {today}")


# Example 4
# This example asks the assistant to create a folder for daily logs if it doesn't already exist.
import os

folder_name = "Daily_Logs"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Daily log folder created.")
else:
    print("Daily log folder already exists.")


# Question 2
# Example 1
# This asks the assistant to display the current date.
import datetime as dt

today = dt.datetime.now()
date_string = today.strftime("%Y-%m-%d")

print(f"Today's date: {date_string}")


# Example 2

import os

folder_name = date_string

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print(f"Folder already exists: {folder_name}")


# Example 3
# This example asks the assistant to store the location of the daily logs folder for other parts of the app.
import datetime as dt
import os

# Getting and formatting today's date
today = dt.datetime.now()
date_string = today.strftime("%Y-%m-%d")

# Creating the daily log folder if necessary
daily_logs_folder = date_string

if not os.path.exists(daily_logs_folder):
    os.mkdir(daily_logs_folder)
    print(f"Created daily log folder: {daily_logs_folder}")
else:
    print(f"Using existing folder: {daily_logs_folder}")

# Storing the location for other parts of the app
print(f"Daily logs will be saved in: {daily_logs_folder}")


# Question 3
# This example asks the assistant to create a Task class that can manage tasks with attributes for name, due date, and status.
class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.__status = "Pending"

    @property
    def status(self):
        return self.__status

    def mark_complete(self):
        self.__status = "Completed"

    def reschedule(self, new_due_date):
        self.due_date = new_due_date

    def display(self):
        print(
            f"Task: {self.name} | "
            f"Due: {self.due_date} | "
            f"Status: {self.status}"
        )


# QQuestion 4

# Let's Create individual task objects
task1 = Task("Complete Python assignment", "2026-10-25")
task2 = Task("Read course materials", "2026-10-26")
task3 = Task("Organize daily logs", "2026-10-27")

# Displaying the original tasks
print("Initial Task List:")
task1.display()
task2.display()
task3.display()

# Updating task information
task1.mark_complete()
task2.reschedule("2026-10-28")

# Displaying the updated tasks
print("\nUpdated Task List:")
task1.display()
task2.display()
task3.display()