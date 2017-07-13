# using recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

n=int(raw_input('Enter a number'))
result = factorial(n)
print result

# n = int(raw_input("Enter a number"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print fact