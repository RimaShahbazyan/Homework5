cache={}
def factorial(n):
    if(n==0):
        return 1
    cache[n]= (factorial(n-1)*n)
    return cache[n]

print(factorial(int(input("input the number to count factorial"))))
