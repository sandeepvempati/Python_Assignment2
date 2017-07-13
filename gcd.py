# from fractions import gcd
# print gcd(17,147)

def gcdp(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(smaller,1,-1):
        if(a%i==0 and b%i==0):
            return i
    return 1

print gcdp(17,147)