a = 0
i = 0
while True:
    b = input("please enter your grade:")
    if b == "exit":
        print("your average is:", avg)
        break
    else:
        i = i + 1
        b = float(b)
        a = a + b
        avg = a/i