#Uses python3

import sys


def acyclic(adj):
    visited=[False for _ in range(len(adj))]
    stack = [False for _ in range(len(adj))]

    def dfs(v):
        visited[v] = True
        stack[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif stack[neighbor]:
                return True
        stack[v]=False
        return False
    
    for node in range(len(adj)):
        if not visited[node]:
            if dfs(node):
                return 1
            
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print(acyclic(adj))
    print(adj)
