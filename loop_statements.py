import random
import math

#The Range Riddle

#Task 1:Your Mood Today

moody = ["happy", "sad", "relaxed", "excited", "joyful", "thankful", "blessed"]
daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
timesofday = ["morning", "afternoon", "evening"]

for i in range(len(daysofweek)):
    print(f"Today is {daysofweek[i]} and my mood is {random.choice(moody)}.")

#2. Double Scoop with Nested Loop

#Task 1:Your Mood Tracker

for i in range(len(daysofweek)):
    for j in range(0, (len(timesofday))):
        print(f"Today is {daysofweek[i]} {timesofday[j]} and my mood is {random.choice(moody)}.")

#3. Loop Condition Logic

#Task 1:Loop Condition Exploration

term_color = "blue"

i = 1
while i != 2: #or term_color == "red":
    print(i, term_color)
    i += 1
    #term = input("Enter term color: ")
    if i == 4:
        break

#Task 2:Conditional Exit

#4. Python's Random GAme Night
    
child_games = ["tag", "hopscotch", "jacks","marbles", "monopoly", "cornhole", "hangman"]

print("Let's try to pick the childhood game the computer chooses!  When done, enter end")
print("The list is as follows: tag, hopscotch, jacks, marbles, monopoly, cornhole, and hangman")

user_choice = input("Enter one of the games above, and see of you match the computer: ")
while user_choice != "end":
    #user_choice = input("Enter one of the games above, and see of you match the computer: ")
    compu_choice = random.choice(child_games)
    if compu_choice == user_choice:
        print(f"You matched the computer with the choice of {user_choice}!")
    else:
        print(f"Your choice of {user_choice} did not match the computer pick of {compu_choice}")
    user_choice = input("Enter one of the games above, and see of you match the computer: ")

#Looping Lists - The Rhythm of Repetition
    
#Task 1:The For Loop DJ Set
    
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 1
for i in range(len(genres)):
    print(f"{genres[i]} is track number {counter} in this set.")
    counter +=1
    
#Task 2:The Remix Artist with while

counter = 1
i = 0

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
while i in range(len(genres)):
    #print(genres[i])
    if genres[i] != "Classical":
        print(f"{genres[i]} is track number {counter} in this set.")
        counter +=1
        i +=1
    else:
        break

#Task 3:Light Show Technician Loop

genres1 = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
count = 1
j = 0

while j in range(0, len(genres1), 1):
    if genres[j] != "Classical": 
        print(f"{genres1[j]} is track number {count} in this set.  The light show is ready!")
        count +=1
        j += 1
    else:
        break


    
#Advanced Looping Techniques

#Task 1:The Selective DJ

genres2 = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
count1 = 1
k = 0

for k in range(0, len(genres2), 1):
    genres3 = slice(1, len(genres2))
    print(genres2[genres3])
    count1 +=1
    k += 1

    if count == 6:
        break 
#print(genres2[genres3])    

#Task 2: The One-Liner Band with List Comprehensions

genres4 = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

genres_listcomp = [x + (' Music') for x in genres4]
print(genres_listcomp)

#Task 3:Numerical Beats with range

z = [1,2,3,4,5,6,7,8,9,10]

countdown = [print(z) for z in range(10, 0, -1)]
print("The beat drops now!")



























































