import heapq
import sys

def dijkstra(n, adj, u, v):
    # Distance to each node initialized to infinity
    dist = [float('inf')] * n
    dist[u] = 0

    # Min-heap priority queue
    pq = [(0, u)]  # (distance, vertex)

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        # If we already found a better path before, skip processing this node
        if current_dist > dist[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in adj[current_vertex]:
            distance = current_dist + weight

            # If found a shorter path to the neighbor, update and push to pq
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Return the shortest distance to v, or -1 if not reachable
    return dist[v] if dist[v] != float('inf') else -1

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n)]

    index = 2
    for _ in range(m):
        u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
        adj[u - 1].append((v - 1, w))
        index += 3

    start = int(data[index]) - 1
    end = int(data[index + 1]) - 1

    result = dijkstra(n, adj, start, end)
    print(result)

if __name__ == "__main__":
    main()