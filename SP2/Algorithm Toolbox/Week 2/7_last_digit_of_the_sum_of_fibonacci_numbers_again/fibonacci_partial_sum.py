# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to < 0:
        return 0
    pisano_period = 60

    to = to % pisano_period
    from_ = from_ % pisano_period

    if from_>to:
        to += pisano_period

    if to == 0:
        return 0

    prev, curr = 0, 1
    for i in range(2, to + 3):
        if i == from_+2:
            first_sum = (curr-1)%10
        prev, curr = curr, (prev + curr) % 10

    second_sum = (curr - 1) % 10
    last_digit_S_n = (second_sum - first_sum) % 10
    return last_digit_S_n


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
