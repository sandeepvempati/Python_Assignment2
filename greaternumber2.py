a = int(raw_input("enter a"))
b = int(raw_input("enter b"))
c = int(raw_input("enter c"))
if(a>b and a>c):
    print "Greatest among three numbers is %d"%a
elif(b>a and b>c):
    print "Greatest among three numbers is %d"%b
else:
    print "Greatest among three numbers is %d"%c
