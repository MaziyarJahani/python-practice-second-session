import random
x = 6
go = input("please say go to roll the dice:")
if go == "go":
    while x == 6:
        x = random.randint (1,6)
        print (x)
    print("finished")
else:
    print ("dear Lord, I said say go")