def fib(n):
    a, b = 0,1
    result = 0
    for i in range (n):
        a,b = b, result
        result = a + b
    return result