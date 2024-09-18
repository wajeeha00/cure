def majority_element_naive(elements):
    elements.sort()
    for i in range(len(elements)):
        j = i+len(elements)//2
        if j<len(elements) and elements[i] == elements[j]:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
