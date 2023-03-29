a = float(input("please insert the time based on seconds:"))
b = 0
c = 0
while a >= 3600:
    a = a - 3600
    b = b + 1
while a >= 60:
    a = a - 60
    c = c + 1
print("the time is:", b , "hours and" , c , "minutes and" , a , "seconds")