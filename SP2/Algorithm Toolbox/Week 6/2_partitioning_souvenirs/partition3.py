from sys import stdin


def partition3(values):
    total_sum = sum(values)
    if total_sum%3 != 0:
        return 0
    target_sum = total_sum/3
    values.sort(reverse=True)
    subsets = [0] * 3

    def checksums(index):
        if index == len(values):
            return subsets[0] == subsets[1] == subsets[2] == target_sum
        
        for i in range(3):
            if subsets[i] + values[index] <= target_sum:
                subsets[i] += values[index]
                if checksums(index + 1):
                    return True
                subsets[i]-=values[index]
            if subsets[i] == 0:
                break

        return False
    return 1 if checksums(0) else 0

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
