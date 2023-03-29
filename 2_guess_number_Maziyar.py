import random
counter = 1
computer_number = random.randint(1 , 50)
print("guess my number")
print("enter a number between 1 to 50")
for i in range (10):
    user_number = int(input())
    if computer_number == user_number:
        print("yeeees 😍")
        print ("you tried", counter , "times and you won.")
        break
    elif computer_number > user_number:
        print("go up ⬆")
        counter = counter + 1
    elif computer_number < user_number:
        print("go down ⬇")
        counter = counter + 1
if computer_number != user_number:
    print ("you lost")
    print ("The Game is Over")