def max_pairwise_product(numbers):
    sort = sorted(numbers)
    return sort[-1]*sort[-2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
