def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


a = int(input("Enter a number: "))
print("Fibonacci number at", a, "is", fibonacci(a))
