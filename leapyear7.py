n = int(raw_input("Enter a year"))
if(n%100==0):
    if(n%400==0):
        print "%d is leap year" %n
    else:
        print "%d is not a leap year" %n
elif(n%4==0):
    print "%d is a leap year"%n
else:
    print "%d is not a leap year" %n