import random
user_score=0
computer_score=0
# for i in range(3):
while computer_score < 3 and user_score < 3:
    x= random.randint (1,3)
    #random.choice() is for "list, sequence and araye ha!" its an easier way
    if x == 1:
        computer_choice = "rock"
    if x == 2:
        computer_choice = "paper"
    if x == 3:
        computer_choice = "scissors"
    user_choice = input()
    print ("💻:", computer_choice)
    print ("🧑:", user_choice)
    if computer_choice == "rock" and user_choice == "paper":
        user_score = user_score + 1
    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score + 1
    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score + 1
    elif computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score + 1
    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score + 1
    elif computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score + 1
    elif computer_choice == user_choice:
        print ("tie")
if computer_score == 3:
    print ("you lost ¯\_(ツ)_/¯")
else:
    print ("you won (T_T)")