from sys import stdin


def min_refills(dist,miles,gas_stations):
    n = len(gas_stations)
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            return -1
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1 
        limit = gas_stations[curr_refill] + miles
        curr_refill += 1
    return num_refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
