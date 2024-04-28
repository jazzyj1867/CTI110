###FrownerJasmine
#04/28/2024
#P4HW1
#ability to edit and enhance exiting programs


'''
Pseudocode for the score entry and grading program:
Ask user to enter for number of scores they would like to enter. 
Create a loop to collect the number of scores the user wants to enter.
Note every time a score is entered, the following should be done
    Evaluate if the score is valid, it should be between 0 and 100 . 
    If it is not, notify the user and ask for a VALID score to be entered.
    If score is valid, add the score to a list. Make sure the score list is given an informative name.
After collecting all the scores.
The program is to display the following:
    Lowest score entered
    Score List after dropping lowest score
The average of scores in modified list
Determine the letter grade for the calculated average and display it to user. .
'''


num_scores = int(input("How many scores do you want to enter? "))
scores = []

for item in range(num_scores):
    score = -1  
    while score < 0:
        #ask until a no negative score is entered
        score = float(input(f"Enter score #{item+1}: "))
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

# get the average and remove the lowest score also
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

# get letter grade based on average 
grade = ""
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("----------------------------------")
