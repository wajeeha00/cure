from sys import setrecursionlimit, stdin, stdout
import threading

setrecursionlimit(10**6)
threading.stack_size(2**26)

def kosaraju_scc(n, adj):
    # Step 1: First DFS to determine finishing times
    def dfs1(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(v)

    # Step 2: Transpose the graph
    def dfs2(v):
        visited[v] = True
        for neighbor in adj_rev[v]:
            if not visited[neighbor]:
                dfs2(neighbor)

    # Prepare to collect results
    stack = []
    visited = [False] * n

    # Step 1: Order vertices by finishing time
    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Step 2: Create the transpose of the graph
    adj_rev = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_rev[v].append(u)

    # Step 3: Process all nodes in reverse finishing order
    visited = [False] * n
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node)
            scc_count += 1

    return scc_count

def main():
    n, m = map(int, stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        adj[u-1].append(v-1)
    
    result = kosaraju_scc(n, adj)
    stdout.write(f"{result}\n")

if __name__ == "__main__":
    threading.Thread(target=main).start()