#Uses python3

import sys
import queue

def bipartite(adj):
    n = len(adj)
    colors = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    def bfs(start):
        q = queue.Queue()
        q.put(start)
        colors[start] = 0  # Start coloring the start vertex with color 0
        
        while not q.empty():
            node = q.get()
            current_color = colors[node]
            next_color = 1 - current_color
            
            for neighbor in adj[node]:
                if colors[neighbor] == -1:  # If not colored
                    colors[neighbor] = next_color
                    q.put(neighbor)
                elif colors[neighbor] == current_color:  # Conflict in coloring
                    return False
        
        return True
        # Check all components (in case the graph is not connected)
    for i in range(n):
        if colors[i] == -1:  # Not colored, meaning it's a new component
            if not bfs(i):
                return 0  # Graph is not bipartite
    
    return 1  # Graph is bipartite
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
