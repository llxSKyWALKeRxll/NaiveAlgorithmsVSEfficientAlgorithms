def gcd(a, b):
    best = 0
    for i in range(1, a + b):
        if a%i==0 and b%i==0:
            best = i
    return best
    
print(gcd(35, 28))
