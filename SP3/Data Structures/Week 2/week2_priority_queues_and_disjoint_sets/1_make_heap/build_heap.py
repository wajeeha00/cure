# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    def parent(i):
        return i//2
    def left_child(i):
        return (2*i)+1
    def right_child(i):
        return (2*i) + 2

    def sift_down(i):
        max_index = i
        l = left_child(i)
        r = right_child(i)
        if l<=len(data)-1 and data[l]<data[max_index]:
            max_index = l
        if r<=len(data)-1 and data[r]<data[max_index]:
            max_index = r
        if i != max_index:
            a = data[i]
            b = data[max_index]
            data[i] = b
            data[max_index] = a 
            swaps.append((i,max_index))
            sift_down(max_index)

    # i = ((len(data)-1)//2)-1
    i = len(data)-1
    while i>=0:    
        sift_down(i)
        i-=1
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
