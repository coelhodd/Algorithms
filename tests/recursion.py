def rec(n):
    print(n)
    if n == 10: # base case
        return
    return rec(n+1)    # the function calls itself altering the input till it reaches the base case

def factorial(n):
    if n == 0: 
        return 1
    return n * factorial(n-1)

rec(1)