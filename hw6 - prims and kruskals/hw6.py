import heapq
import time
from collections import defaultdict

import networkx as nx
import numpy as np


def kruskals_mst(G):
    start_time = time.time()
    min_spanning_tree = []
    mst_weight, index, mst_edges = 0, 0, 0

    G = sorted(G, key=lambda edge: edge[2])
    parent_list = []
    rank_list = []
    n_vertices_dict = find_total_vertices(G)

    for node in range(n_vertices_dict):
        rank_list.append(0)
        parent_list.append(node)

    while mst_edges < n_vertices_dict - 1:
        u, v, weight = G[index]
        index = index + 1
        u = find_root(parent_list, u)
        v = find_root(parent_list, v)
        if u != v:
            mst_edges = mst_edges + 1
            min_spanning_tree.append((u, v))
            mst_weight = mst_weight + weight
            union_by_rank(parent_list, rank_list, u, v)
    return mst_weight, min_spanning_tree, time.time() - start_time


def find_root(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find_root(parent, parent[vertex])


def union_by_rank(parent_list, rank_list, u, v):
    root_of_u = find_root(parent_list, u)
    root_of_v = find_root(parent_list, v)
    if rank_list[root_of_u] < rank_list[root_of_v]:
        parent_list[root_of_u] = root_of_v
    elif rank_list[root_of_u] > rank_list[root_of_v]:
        parent_list[root_of_v] = root_of_u
    else:
        parent_list[root_of_v] = root_of_u
        rank_list[root_of_u] += 1


def find_total_vertices(G):
    default_dictionary = defaultdict(list)
    for u, v, weight in G:
        default_dictionary[u].append((v, weight))
        default_dictionary[v].append((u, weight))
    len_of_dict = len(default_dictionary)
    return len_of_dict


def prims_mst(G):
    start_time = time.time()
    dict_storage = defaultdict(list)

    init_values = G[0][0]
    source_values = G[0][0]
    for i, j, edge_weight in G:
        dict_storage[i].append((j, edge_weight))
        dict_storage[j].append((i, edge_weight))
    min_spanning_tree = []
    path_weight_from_vertex = {}
    heap_storage = [(0, init_values, source_values)]
    path_cost = 0
    is_edge_observed = False

    while heap_storage:
        weight, u, source_values = heapq.heappop(heap_storage)
        if u in path_weight_from_vertex:
            continue
        else:
            path_weight_from_vertex[u] = weight
            path_cost += weight
        if is_edge_observed:
            min_spanning_tree.append((source_values, u))
        is_edge_observed = True
        for pp, qq in dict_storage[u]:
            if pp not in path_weight_from_vertex:
                heapq.heappush(heap_storage, (qq, pp, u))
    return path_cost, min_spanning_tree, time.time() - start_time


def create_random_w_graph(n):
    p = 2 / n * np.log(n)
    lib_G = nx.gnp_random_graph(n, p)
    G = []
    for u, v in lib_G.edges:
        G.append((u, v, np.random.randint(1, 1000)))
    return G


if __name__ == '__main__':
    k_times, p_times = [], []
    # template = "{0:>15}|{1:>15}|{2:>15}|{3:>15}|{4:>20}"  # column widths: 8, 10, 15, 7, 10
    # print(template.format("ALGORITHM", "NODES IN GRAPH", "EDGES IN MST", "MST WEIGHT", "TIME TAKEN (in s)"))
    for i in range(1100, 2001, 100):
        G = create_random_w_graph(i)
        cost, mst, time_k = kruskals_mst(G)
        # print(template.format("Kruskal's", i, len(mst), cost, time_k))
        k_times.append(time_k)
        cost, mst, time_p = prims_mst(G)
        p_times.append(time_p)
        # print(template.format("Prim's", i, len(mst), cost, time_p))
        print(i)

    for i in range(len(k_times)):
        print(k_times[i])

    print("------------")
    for i in range(len(k_times)):
        print(p_times[i])
