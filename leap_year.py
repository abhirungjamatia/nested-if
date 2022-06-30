y=int(input("enter year"))
if y%100==0 and y%400==0:
    print("it is a century Leap year")
    if y%4==0:
        print("it is a leap year")
    else:
        print("it is century but not a leap year")
else:
    print("it is not a leap year")