fiboList = [0, 1]
def fibonacci(n):
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            fiboList.append(fiboList[i - 1] + fiboList[i - 2])
    return fiboList[n]
        


a = int(input("Enter a number: "))
print("Fibonacci number at", a, "is", fibonacci(a))
