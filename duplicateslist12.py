li=[]
for i in range(int(raw_input("enter a number of values in list"))):
   li.append(raw_input(""))

s=[]
for i in li:
    if i not in s:
        s.append(i)

print s

# print set(li)
