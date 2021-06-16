def gcd(a, b):
    if b == 0:
        return a
    lemma = a % b
    return gcd (b, lemma)
    
print(gcd(35, 28))
