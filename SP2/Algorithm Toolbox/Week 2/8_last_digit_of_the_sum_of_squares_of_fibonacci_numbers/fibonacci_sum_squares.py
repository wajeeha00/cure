def fib(n):
    n = n % 60

    if n <= 1:
        return n

    prv1 = 0
    prv2 = 1

    for i in range(2, n+1):
        cur = prv1 + prv2
        prv1 = prv2
        prv2 = cur

    return prv2

n = int(input())

fib_n = fib(n)
fib_n_1 = fib(n+1)

# print(fib_n)
# print(fib_n_1)

lst = (fib_n * fib_n_1) % 10
print(lst)