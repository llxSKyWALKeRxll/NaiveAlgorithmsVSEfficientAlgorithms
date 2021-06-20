def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    euc = gcd(a, b)
    return int(a*b / euc)
    

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
