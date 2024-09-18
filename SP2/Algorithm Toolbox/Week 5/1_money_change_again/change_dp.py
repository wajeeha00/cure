def change(money):
    denominations = [1,3,4]
    min_num_coins = [0]
    for i in range(1, money+1):
        min_num_coins.append(99999999)
        for denom in denominations:
            if i >= denom:
                coins = min_num_coins[i-denom]+1
                if coins<min_num_coins[-1]:
                    min_num_coins[-1] = coins
    return min_num_coins[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
