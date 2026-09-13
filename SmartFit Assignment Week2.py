# A Basic Fitness Program Eligibility Checker
# 13/09/2026

#   Question 1:
# First let's ask the user for his/her age to know the fitness program they are eligible for.
print("Welcome to SmartFit! Let's find out which fitness program you are eligible for based on your age.")

age = int(input("Kindly Enter your age: "))

if age < 18:
    print("You are eligible for the Teen Fitness Program.")
elif age <= 40:
    print("You are eligible for the Regular Fitness Program.")
else:
    print("You are eligible for the Senior Wellness Program.")

# For that, an age below 18 goes into the first block.
# If that is false, Python checks whether the age is 40 or below. 
# If that is also false, the `else` block handles ages above 40.


# Question 2:
# Next, let's ask the user if they have any medical conditions
print ("Now, we need to know if you have any medical conditions, that will assist in determining your eligibility.")
medical_condition = input(
    "Do you have any medical conditions? (reply with either 'yes' or 'no'): "
).lower()

if medical_condition not in ["yes", "no"]:
    print(medical_condition, "is your input which is invalid. Enter 'yes' or 'no'.")
elif age >= 40 and medical_condition == "yes":
    print("Medical clearance required before joining.")
elif age < 40 or medical_condition == "no":
    print("You can proceed with your registration.")

# For example, if the user is 45 and enters `yes`, both parts of the `and` condition are true, so medical clearance is required. 
# But, if the user is 25 and enters `yes`, the first condition is false because the user is not 40 or older, so the program allows registration



# Question 3:
# Membership selection and additional options based on their choice.
# Finally, let's ask the user to choose a membership plan and provide additional options based on their choice.
print("Now, let's choose a membership plan for you.")

membership = input(
        "Choose membership reply with 'Basic' or 'Premium': "
    ).lower()

if membership == "basic":
        personal_training = input(
            "Do you want personal training? reply with 'yes' or 'no': "
        ).lower()

        if personal_training == "yes":
            print("Basic plan with personal training: $45 per month.")
        elif personal_training == "no":
            print("Basic plan: $30 per month.")
        else:
            print(personal_training, "is your input which is invalid. Please enter 'yes' or 'no'.")

# Nested condition with logical operator
        if personal_training == "no":
            print("Consider upgrading to Premium for more benefits!")

elif membership == "premium":
        print("Premium plan: $60 per month.")

# Nested conditions for Premium members
        if age < 30:
            print("You qualify for a youth discount! 10% off your plan.")

        if medical_condition == "yes":
            print("We recommend a free consultation before starting.")

else:
        print("Invalid membership. Please choose Basic or Premium.")
