def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
def countways(s):
    return fib(s+1)
n=int(input("enter a number"))
print("number os ways=")
print(countways(n))
