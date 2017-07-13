from collections import Counter
li=[]
for i in range(int(raw_input("enter a list of values"))):
    li.append(raw_input())
print li
x=set(li)

print dict((i,li.count(i)) for i in x)

# for i in x:
#     print i,li.count(i)

# print Counter(li) # using Counter function