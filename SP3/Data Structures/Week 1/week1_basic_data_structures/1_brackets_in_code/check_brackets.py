# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            index.append(i+1)
        elif next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
                index.pop()
            else:
                return i+1
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return index[0]



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
