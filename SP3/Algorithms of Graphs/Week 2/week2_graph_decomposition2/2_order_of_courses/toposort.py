#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


# def toposort(adj):
#     used = [0] * len(adj)
#     order = []
#     #write your code here
#     return order

def toposort(adj):
    in_deg = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            in_deg[j]+=1
    queue = [i for i in range(len(adj)) if in_deg[i]==0]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)

        for v in adj[u]:
            in_deg[v]-=1
            if in_deg[v]==0:
                queue.append(v)

    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
