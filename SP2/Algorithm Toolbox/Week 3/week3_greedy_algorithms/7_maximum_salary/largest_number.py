from functools import cmp_to_key

def custom_compare(x, y):
    # Compare two strings by their concatenated results
    if x + y > y + x:
        return -1
    else:
        return 1

def largest_number(numbers):
    # Convert all integers to strings
    numbers = list(map(str, numbers))
    
    # Sort numbers using the custom comparator
    numbers.sort(key=cmp_to_key(custom_compare))
    
    # Concatenate the sorted numbers
    largest_num = ''.join(numbers)
    
    
    if largest_num[0] == '0':
        return '0'
    
    return largest_num

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    
    print(largest_number(numbers))