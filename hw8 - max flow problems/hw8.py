import copy
import time
from collections import defaultdict

import networkx as nx
import numpy as np
from heapdict import heapdict


def max_flow_edmund_karp_fat_pipes(source, sink, G):
    start_time = time.time()
    edges = defaultdict(lambda: defaultdict(lambda: 0))
    for u, v, w in G:
        edges[u][v] = max(edges[u][v], w)
        edges[v][u] = max(edges[v][u], 0)
    copy_edges = copy.deepcopy(edges)
    max_flow = 0
    while True:
        parent, min_flow = dijkstra_with_fat(source, sink, edges)
        if parent is None:
            result = maximum_flow_graph(copy_edges, edges)
            return max_flow, result, time.time() - start_time

        max_flow = max_flow + min_flow
        aug_path_update(source, sink, edges, parent, min_flow)


def dijkstra_with_fat(source, sink, edges):
    default_dict = defaultdict()
    heap_dict = heapdict()
    heap_dict[source] = -1 << 30
    default_dict[source] = 1 << 30
    visited = set()
    parent = defaultdict()

    while heap_dict != []:
        try:
            u, w = heap_dict.popitem()
        except:
            return None, 0

        visited.add(u)
        if u == sink:
            return parent, default_dict[u]
        for v, weight in edges[u].items():
            if v not in visited and weight:
                default_dict[v] = min(default_dict[u], weight)
                heap_dict[v] = -default_dict[v]
                parent[v] = (u, weight)


def maximum_flow_graph(edges, residual_edges):
    residual_values = []
    for u, next in edges.items():
        for v, capacity in next.items():
            check = capacity - residual_edges[u][v]
            if check > 0:
                residual_values.append((u, v, check))
    return residual_values


def aug_path_update(source, sink, edges, parent, min_flow):
    v = sink
    while v != source:
        u, w = parent[v]
        edges[u][v] = edges[u][v] - min_flow
        edges[v][u] = edges[v][u] + min_flow
        v = u


# -----------------------------------------------------------------------------------------------------------------------

def max_flow_dinitz_short_pipes(source, sink, G):
    start_time = time.time()
    edges = defaultdict(lambda: defaultdict(lambda: 0))
    for u, v, w in G:
        edges[u][v] = max(edges[u][v], w)
        edges[v][u] = max(edges[v][u], 0)
    import copy
    edges_copy = copy.deepcopy(edges)
    max_flow = 0

    while True:
        parent = bfs(source, sink, edges)
        if parent is None:
            result = maximum_flow_graph(edges_copy, edges)
            return max_flow, result, time.time() - start_time

        min_flow = 1 << 30
        v = sink
        while v != source:
            u, w = parent[v]
            min_flow = min(min_flow, w)
            v = u
        max_flow = max_flow + min_flow
        aug_path_update(source, sink, edges, parent, min_flow)


def bfs(source, sink, edges):
    queue = [source]
    visited = set()
    visited.add(source)
    dict = defaultdict()
    while queue:
        u = queue.pop(0)
        if u == sink:
            return dict

        for v, w in edges[u].items():
            if v not in visited and w:
                queue.append(v)
                visited.add(v)
                dict[v] = (u, w)


def create_random_w_graph(n):
    p = 2 / n * np.log(n)
    lib_G = nx.gnp_random_graph(n, p, directed=True)
    G = []
    for u, v in lib_G.edges:
        G.append((u, v, np.random.randint(1, 101)))
    return G, lib_G


if __name__ == '__main__':
    print("---------------------------Example 1: Fat Pipes:---------------------------")
    print(max_flow_edmund_karp_fat_pipes(0, 3, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print("---------------------------Example 2: Fat Pipes:---------------------------")
    print(
        max_flow_edmund_karp_fat_pipes(0, 4,
                                       [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
    print("---------------------------Example 1: Short Pipes:---------------------------")
    print(max_flow_dinitz_short_pipes(0, 3, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print("---------------------------Example 2: Short Pipes:---------------------------")
    print(
        max_flow_dinitz_short_pipes(0, 4,
                                    [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))

    avg_fat_times = []
    avg_short_times = []
    for x in range(1):
        fat_times, short_times = [], []
        template = "{0:>15}|{1:>15}|{2:>10}|{3:>20}"  # column widths: 8, 10, 15, 7, 10
        print(template.format("ALGORITHM", "NODES IN GRAPH", "MAX FLOW", "TIME TAKEN (in s)"))
        for i in range(100, 1001, 100):
            G, lib_G = create_random_w_graph(i)
            source = np.random.choice(lib_G.nodes(), 1)[0]
            u = source
            for j in range(10000):
                u = np.random.choice(list(lib_G.neighbors(u)), 1)[0]
            sink = u

            G_short = G.copy()
            max_flow_fat, result1, time_fat = max_flow_edmund_karp_fat_pipes(source, sink, G)
            print(template.format("Fat pipes", i, max_flow_fat, time_fat))
            fat_times.append(time_fat)
            max_flow_short, result2, time_short = max_flow_dinitz_short_pipes(source, sink, G_short)
            short_times.append(time_short)
            print(template.format("Short pipes", i, max_flow_short, time_short))

        avg_fat_times.insert(x, fat_times)
        avg_short_times.insert(x, short_times)

    # for i in range(len(fat_times)):
    #     print(fat_times[i])
    #
    # print("------------")
    # for i in range(len(fat_times)):
    #     print(short_times[i])

    print(np.array(avg_fat_times).shape)
    print(np.array(avg_short_times).shape)

    print(np.array(avg_fat_times).mean(axis=0))
    print(np.array(avg_short_times).mean(axis=0))
