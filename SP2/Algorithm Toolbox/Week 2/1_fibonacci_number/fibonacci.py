def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        seq = [0,1]
        for i in range(2, n+1):
            seq.append(seq[i-1]+seq[i-2])
        return seq[-1]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))