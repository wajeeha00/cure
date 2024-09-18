#Uses python3

import sys
import queue

from collections import deque

def distance(adj, start, goal):
    n = len(adj)
    dist = [-1] * n  # -1 means unvisited
    dist[start] = 0
    q = deque([start])
    
    while q:
        node = q.popleft()
        current_distance = dist[node]
        
        if node == goal:
            return current_distance
        
        for neighbor in adj[node]:
            if dist[neighbor] == -1:  # Not visited
                dist[neighbor] = current_distance + 1
                q.append(neighbor)
    
    return -1  # If goal is not reachable

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
