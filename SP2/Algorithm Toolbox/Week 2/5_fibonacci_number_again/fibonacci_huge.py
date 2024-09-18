def pisanoPeriodandLast(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibonacci_huge_naive(n, m):
    period = pisanoPeriodandLast(m)
    n = n%period
    if n <= 1:
        return n%m
    else:
        seq = [0,1]
        for i in range(2, n+1):
            seq.append(seq[i-1]+seq[i-2])
        return seq[-1]%m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
