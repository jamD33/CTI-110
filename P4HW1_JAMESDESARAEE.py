# Desarae James
# P4HW1
# 10/27/26
# Assess ability to edit and enhance programs

'''
Input the number of scores
The scores should be between 0 and 100 
If it is not, notify and ask for a valid score
'''

# Ask the user to input the number of scores the would like to enter
num_scores = int(input("How many scores would you like to enter?"))

scores_list = []

# Collect the exact number of scores requested
for i in range(num_scores):
    score = float(input(f"Enter score #{i +1}: "))

    # Validate score
while score < 0 or score > 100:
    print("Invalid score! Score must be between 0 and 100.")
    score = float(input(f"Please enter a VALID score for #{i + 1}: "))

    # Once validated, add the score to our list
    scores_list.append(score)

    print("--- Processing Results ---")

# Find and display the lowest score
lowest_score = min(scores_list)
print(f"Lowest score entered: {lowest_score}")

# Create a list by dropping the lowest score
modified_scores_list = scores_list.copy()
modified_scores_list.remove(lowest_score)
print("Score list after dropping lowest score: {modified_scores_list}")

# Calculate the average of modified list
if len(modified_scores_list) > 0:
    modified_average = sum(modified_scores_list) / len(modified_scores_list)
else:
    modified_average = 0

print("The average of scores in modified list: {modified_average}")

# Determine and display the letter grade based on modified average 
if modified_average >= 90:
    letter_grade = 'A'
if modified_average >= 80:
    letter_grade = 'B'
if modified_average >= 70:
    letter_grade = 'C'
if modified_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Letter grade for the calculated average: {letter_grade}")