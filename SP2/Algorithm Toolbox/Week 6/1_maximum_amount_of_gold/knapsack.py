from sys import stdin


def maximum_gold(capacity, weights):
    golds = [0] + weights
    gold_dict = {}
    for i in range(0, capacity+1):
        gold_dict[(i, 0)] = 0
    for i in range(0, len(golds)):
        gold_dict[(0, i)] = 0

    for i in range(1, len(golds)):
        for weight in range(1, capacity+1):
            gold_dict[(weight, i)] = gold_dict[(weight, (i-1))]
            if golds[i] <= weight:
                val = gold_dict[(weight-golds[i], i-1)] + golds[i]
                if gold_dict[(weight, i)] < val:
                    gold_dict[(weight, i)] = val
    return max(gold_dict.values())


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
