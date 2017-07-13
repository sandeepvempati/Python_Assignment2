li =[]
for i in range(int(raw_input("enter the length of list"))):
    li.append(raw_input())

if len(li)>0:
    print "List is not empty %s"%li
else:
    print "List is empty %s" %li