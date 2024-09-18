def gcd(a, b):
    if a==0:
        return b
    elif b==0:
        return a
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

def lcm(a, b):
    return (a//gcd(a,b))*b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

