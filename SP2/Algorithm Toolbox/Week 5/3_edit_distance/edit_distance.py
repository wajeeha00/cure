def edit_distance(first_string, second_string):
    array = [[0 for j in range(len(first_string)+1)] for i in range(len(second_string)+1)]
    array[0] = [i for i in range(len(first_string)+1)]
    for i in range(len(second_string)+1):
        array[i][0] = i

    for i in range(1,len(second_string)+1):
        for j in range(1,len(first_string)+1):
            if second_string[i-1] == first_string[j-1]:
               array[i][j] = min(array[i-1][j]+1, array[i][j-1]+1, array[i-1][j-1])
            else:
               array[i][j] = min(array[i-1][j]+1, array[i][j-1]+1, array[i-1][j-1]+1) 
    return array[-1][-1]
if __name__ == "__main__":
    print(edit_distance(input(), input()))
