## This algorithm calculates a minimum spanning tree


def find(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i


def union(i, j, parent):
    a = find(i, parent)
    b = find(j, parent)
    parent[a] = b


def kruskals(cost, parent, V):
    INF = float('INF')
    mincost = 0

    for i in range(V):
        parent[i] = i

    edge_count = 0

    # For each edge
    while edge_count < V - 1:
        min = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                # If i and j are not part of the same set/tree and the is the smallest cost
                if find(i, parent) != find(j, parent) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b, parent)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min

    # Print cost of minimum spanning tree
    print("Minimum cost= {}".format(mincost))


# Prims algortihm

def prims(graph, V):
    selected = [False] * V
    edges = 0
    INF = float('INF')
    totalMin = 0

    # Start with first vertex
    selected[0] = True
    while edges < V - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    # not selected and there is an edge
                    if (not selected[j]) and graph[i][j]:
                        # check if edge is minimum
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j
        totalMin += minimum
        print(str(x) + "-" + str(y) + ":" + str(graph[x][y]))
        selected[y] = True
        edges += 1
    print(totalMin)
