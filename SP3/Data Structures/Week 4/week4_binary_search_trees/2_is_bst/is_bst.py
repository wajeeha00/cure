import sys, threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def IsBinarySearchTree(tree):
    if len(tree) == 0 or len(tree) == 1:
        return True
        
    result = []
    curNode = 0
    stack = []

    while True:
        if curNode != -1:
            stack.append(curNode)
            curNode = tree[curNode][1]
        else:
            if not stack:
                break

            curNode = stack.pop()
            result.append(tree[curNode][0])
            curNode = tree[curNode][2]

    
    for i in range(len(result)-1):
        if result[i] > result[i+1]:
            return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    # print(tree)

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()