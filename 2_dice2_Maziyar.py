import random
while True:
    go = input("please say go to roll the dice:")
    if go == "go":
        x = random.randint (1,6)
        print (x)
        if x < 6:
            print("finished")
            break
    else:
        print ("dear Lord, I said say go")