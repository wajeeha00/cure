import math

class Node:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.parent = c
        self.rank = 0

class Edge:
    def __init__(self, a, b, c):
        self.u = a
        self.v = b
        self.weight = c

def MakeSet(i, nodes, x, y):
    nodes.append(Node(x[i], y[i], i))

def weight(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def Find(i, nodes):
    if i != nodes[i].parent:
        nodes[i].parent = Find(nodes[i].parent, nodes)
    return nodes[i].parent

def Union(u, v, nodes):
    r1 = Find(u, nodes)
    r2 = Find(v, nodes)
    if r1 != r2:
        if nodes[r1].rank > nodes[r2].rank:
            nodes[r2].parent = r1
        else:
            nodes[r1].parent = r2
            if nodes[r1].rank == nodes[r2].rank:
                nodes[r2].rank += 1

def minimum_distance(x, y):
    result = 0.0
    n = len(x)
    nodes = []
    for i in range(n):
        MakeSet(i, nodes, x, y)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append(Edge(i, j, weight(x[i], y[i], x[j], y[j])))
    edges = sorted(edges, key=lambda edge: edge.weight)
    for edge in edges:
        if Find(edge.u, nodes) != Find(edge.v, nodes):
            result += edge.weight
            Union(edge.u, edge.v, nodes)
    return result

if __name__ == '__main__':
    # Read the number of nodes
    n = int(input().strip())
    
    # Read the coordinates
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    # Compute and print the minimum distance
    print("{:.9f}".format(minimum_distance(x, y)))