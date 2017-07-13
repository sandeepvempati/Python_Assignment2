li=[]

for i in range(int(raw_input("enter a number of values in list"))):
    li.append(int(raw_input()))

def multiple(li):
    x = 1
    for i in li:
        x = x*i
    return x

print multiple(li)

