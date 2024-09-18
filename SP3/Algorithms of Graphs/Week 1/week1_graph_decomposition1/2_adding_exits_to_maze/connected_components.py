def number_of_components(n, visited, adj):
    result = 0
    for i in range(n):
        if not visited[i]:
            result += 1
            visited[i] = True
            for node in adj[i]:
                if not visited[node]:
                    connected_comp(visited, node, adj)

    return result


def connected_comp(visited, x, adj):
    visited[x] = True
    for node in adj[x]:
        if not visited[node]:
            connected_comp(visited, node, adj)


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        edges.append((x, y))

    adj = [[] for _ in range(n)]
    visited = [(0) for _ in range(n)]


    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(number_of_components(n, visited, adj))