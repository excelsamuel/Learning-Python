# Week 4 Disscussion Assignment
# 25/09/2026

# Fitness Tracker using functions
# Let's create a simple fitness tracker that calculates the average steps, calories burned, and exercise minutes for a week. 
# We'll also check if the user has achieved their daily step goal.

# Here we start by defining a function to calculate the weekly average of steps, calories, and exercise minutes.
def weekly_average(steps, calories, minutes):
    average_steps = sum(steps) / len(steps)
    average_calories = sum(calories) / len(calories)
    average_minutes = sum(minutes) / len(minutes) 

    return average_steps, average_calories, average_minutes

# Next, we define a function to check if the user has achieved their daily step goal.
# The default target is set to 9000 steps, but it can be adjusted if needed.
def check_goal(daily_steps, target=9000):
    return daily_steps >= target

# Lastly, we define a function to summarise the user's performance for the week.
def summary_of_performance(steps, calories, minutes):
    print("Average steps:", steps)
    print("Average calories burned:", calories)
    print("Average exercise minutes:", minutes)

# we now need to provide some data to use these functions with some sample data for a week.
daily_steps = [5500, 8000, 7000, 9000, 6000, 11000, 7800]
daily_calories = [210, 350, 200, 300, 250, 450, 320]
daily_minutes = [20, 35, 30, 45, 25, 45, 30]

# Now we can call the functions to calculate the weekly averages and check if the user did it!
average_steps, average_calories, average_minutes = weekly_average(
    daily_steps, daily_calories, daily_minutes
)

# User's performance for the week
summary_of_performance(average_steps, average_calories, average_minutes)

# Check if the user has achieved their daily step goal
print("Your goal is achieved: ", check_goal(7000, target=9000))