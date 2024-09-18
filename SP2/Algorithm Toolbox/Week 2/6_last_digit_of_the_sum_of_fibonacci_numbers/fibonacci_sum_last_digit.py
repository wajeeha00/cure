def fibonacci_sum(n):
    if n < 0:
        return 0

    pisano_period = 60

    n = n % pisano_period

    if n == 0:
        return 0

    prev, curr = 0, 1
    for _ in range(2, n + 3):
        prev, curr = curr, (prev + curr) % 10

    last_digit_S_n = (curr - 1) % 10
    return last_digit_S_n


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
