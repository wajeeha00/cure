from sys import stdin

def best_item(weights, values):
    max_val_per_weight = 0
    best_item = 0
    for i in range (len(weights)):
        if weights[i]>0:
            if values[i]/weights[i] > max_val_per_weight:
                max_val_per_weight = values[i]/weights[i]
                best_item = i
    return best_item

def optimal_value(capacity, weights, values):

    for _ in range(len(weights)):
        if capacity == 0:
            return value
        i = best_item(weights, values)
        a = min(capacity, weights[i])
        if a > 0:
            value = value + (a*(values[i]/weights[i]))
            weights[i]-=a
            capacity-=a
        else:
            return value
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
