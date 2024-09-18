# python3

import sys
import threading

def find_height(start_node, tree):
    if len(tree[start_node]) == 0:
        return 0
    else:
        height = 1 + max(find_height(node, tree) for node in tree[start_node])
        return height
    
def compute_height(n, parents):
    max_height = 0
    nodes = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    max_height = 1+find_height(root, nodes)


    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
