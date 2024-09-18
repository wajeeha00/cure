from bisect import bisect_left, bisect_right

def main():
    M = 1000000001
    sorted_list = []
    last_sum_result = 0
    results = []

    def add(i):
        value = (i + last_sum_result) % M
        if value not in sorted_list:
            # Insert and keep sorted
            pos = bisect_left(sorted_list, value)
            sorted_list.insert(pos, value)
    
    def delete(i):
        value = (i + last_sum_result) % M
        pos = bisect_left(sorted_list, value)
        if pos < len(sorted_list) and sorted_list[pos] == value:
            sorted_list.pop(pos)
    
    def find(i):
        value = (i + last_sum_result) % M
        pos = bisect_left(sorted_list, value)
        if pos < len(sorted_list) and sorted_list[pos] == value:
            results.append("Found")
        else:
            results.append("Not found")
    
    def range_sum(l, r):
        l_val = (l + last_sum_result) % M
        r_val = (r + last_sum_result) % M

        if l_val <= r_val:
            left_index = bisect_left(sorted_list, l_val)
            right_index = bisect_right(sorted_list, r_val)
            sum_result = sum(sorted_list[left_index:right_index])
        else:
            # Range wraps around
            left_index = bisect_left(sorted_list, l_val)
            right_index = bisect_right(sorted_list, r_val)
            sum_result = sum(sorted_list[left_index:]) + sum(sorted_list[:right_index])
        
        results.append(str(sum_result))
        return sum_result
    
    # Read number of operations
    n = int(input().strip())
    
    # Process each operation
    for _ in range(n):
        operation = input().strip().split()
        op_type = operation[0]
        a = int(operation[1])
        
        if op_type == '+':
            add(a)
        elif op_type == '-':
            delete(a)
        elif op_type == '?':
            find(a)
        elif op_type == 's':
            last_sum_result = range_sum(a, int(operation[2]))
    
    # Print all results
    print("\n".join(results))

if __name__ == "__main__":
    main()