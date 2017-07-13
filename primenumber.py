n = int(raw_input("enter a number"))

if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print n,"is not a prime number"
            print (i,"*",n/i,"is",n)
            break
    else:
        print "%d is prime number" %n

else:
    print "It is not a prime number"
