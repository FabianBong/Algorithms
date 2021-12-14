## This algorithm serves to calculate the shortest path between one vertex and all other vertecies
from queue import PriorityQueue


def initialize(V):
    INF = float('inf')
    dist = [INF] * V
    pred = [None] * V
    return dist, pred


def relax(u, v, graph, dist, pred):
    t = dist[u] + graph[u][v]
    if t < dist[v]:
        dist[v] = t
        pred[v] = u
        return True
    return False


def bellman_ford(graph, V, src):
    dist, pred = initialize(V)
    dist[src] = 0

    for i in range(V - 1):
        for j in range(V):
            for k in range(V):
                if graph[j][k] != 0:
                    relax(j, k, graph, dist, pred)

    return dist


def dijkstra(graph, V, src):
    dist, pred = initialize(V)
    dist[src] = 0
    visited = [False] * V

    q = PriorityQueue()
    q.put((0, src))

    while not q.empty():
        (d, cur) = q.get()
        visited[cur] = True

        for neighbor in range(V):
            if graph[cur][neighbor] != 0:
                new_dist = graph[cur][neighbor]
                if not visited[neighbor]:
                    t = dist[cur] + graph[cur][neighbor]
                    if t < dist[neighbor]:
                        q.put((t, neighbor))
                        dist[neighbor] = t
                        pred[neighbor] = cur
    return dist
