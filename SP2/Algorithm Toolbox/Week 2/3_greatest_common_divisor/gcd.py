def gcd(a, b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
