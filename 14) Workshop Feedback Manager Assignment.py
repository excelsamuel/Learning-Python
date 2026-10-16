# 16/10/2026
# Question 1: Workshop Feedback Manager Assignment

raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
print("This is the Raw Feedback: ", raw_feedback)

# Removing the whitespace and convert to lowercase
cleaned_feedback = raw_feedback.strip().lower()
print("Removed Whitespace and Converted to Lowercase: ", cleaned_feedback)

# Replace "speaker" with "presenter"
cleaned_feedback = cleaned_feedback.replace("speaker", "presenter")
print("Replaced Speaker With Presenter : ", cleaned_feedback)

# Removing more internal spaces
cleaned_feedback = " ".join(cleaned_feedback.split())

# Converting the cleaned text to title case
cleaned_feedback = cleaned_feedback.title()
print("Converted to Title Case: ", cleaned_feedback)

# Display the final result using an f-string
print(f"Cleaned Feedback using f-string: {cleaned_feedback}")


# Question 2:

feedback_list = [
    cleaned_feedback,
    "The Workshop Was Informative And Well Organised",
    "The Examples Were Great And Easy To Understand"
]

# Let's write the initial feedback messages
with open("feedback.txt", "w", encoding="utf-8") as file:
    for feedback in feedback_list:
        file.write(feedback + "\n")

print("Initial Feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Adding another feedback message using append mode 'a'
with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write("The Presenter Answered Questions Clearly\n")

# Reading my complete updated file
print("\nUpdated Feedback:")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# Question 3:

try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        print("Reading Feedback:")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")

except PermissionError:
    print("Permission denied. Close the file and try again.")

finally:
    print("Operation completed.")


# Question 4:

# Read all our feedback entries
with open("feedback.txt", "r", encoding="utf-8") as file:
    feedback_lines = file.readlines()

total_feedback = len(feedback_lines)

# Let's count entries containing "great"
great_count = 0
for line in feedback_lines:
    if "great" in line.lower():
        great_count += 1

# Creating our summary report
summary = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback}\n"
    f"Mentions of 'Great': {great_count}\n"
)

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Print the same report on the console
print(f"\n{summary}")
