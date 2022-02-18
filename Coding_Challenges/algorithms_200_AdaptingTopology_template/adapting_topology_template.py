#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml
import queue

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}

def minEdgeBFS(edges, u, v, n):

    # visited[n] for keeping track
    # of visited node in BFS
    visited = [0] * n

    # Initialize distances as 0
    distance = [0] * n

    # queue to do BFS.
    Q = queue.Queue()
    distance[u] = 0

    Q.put(u)
    visited[u] = True
    while (not Q.empty()):
        x = Q.get()

        for i in range(len(edges[x])):
            if (visited[edges[x][i]]):
                continue

            # update distance for i
            distance[edges[x][i]] = distance[x] + 1
            Q.put(edges[x][i])
            visited[edges[x][i]] = 1
    return distance[v] - 1

def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    return 2*minEdgeBFS(graph, cnot.wires[0], cnot.wires[1], len(graph.keys()))
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")


#
# def n_swaps(cnot):
#         control = cnot.wires[0]
#         target = cnot.wires[1]
#
#
#         if target in graph[control]:
#             return 0
#
#         num_swaps = 1
#         found = False
#         while not Found:
#             no_swap_back=[]
#             for new_control in graph[control]
#
#     def get_swap_paths(c, t):
#         if t in graph[c]:
#             return []
#
#         new_controls = set(graph[c]).difference(set([c]))
#         for new_c in new_controls
#
#
#
#
#     def add_swaps(c, t, no_swap_back=None):
#         print(f'trying {t} in node {c}, ignoring {no_swap_back}')
#         current_targets = set(graph[c]).difference(set([no_swap_back]))
#
#         if len(current_targets) == 0:
#             return 0
#
#         if t in current_targets:
#             print(f'found {t} in {current_targets}')
#             return 0
#
#         print(f'{t} NOT in {current_targets}')
#         search_nodes = current_targets
#         no_swap_back = c
#         print(f'search nodes: {search_nodes}')
#         new_swaps = []
#         for new_c in search_nodes:
#             print(f'new c: {new_c}')
#             new_swaps.append(add_swaps(new_c, t, no_swap_back) + 1)
#
#         if add_swaps(control, target) == 0:
#             return 0
#
#         for new_control in graph[control]:
#             return add_swaps(target, new_control)
