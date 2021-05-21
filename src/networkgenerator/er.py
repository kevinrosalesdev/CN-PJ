import networkx as nx
import random

from itertools import combinations


def generate_ER(N, p):
    if p < 0 or p > 1:
        print("[WARNING]: Probability (parameter p) should be between 0 and 1.")
        return
    if N <= 0:
        print("[WARNING]: Nodes number (parameter N) should be greater than 0.")
        return

    g = nx.Graph()
    g.add_nodes_from(list(range(N)))
    possible_edges = combinations(list(range(N)), 2)
    for edge in possible_edges:
        if random.random() < p:
            g.add_edge(*edge)

    for node in nx.isolates(g):
        while True:
            n = random.randrange(len(g.nodes()))
            if n != node:
                break

        g.add_edge(node, n)

    while not nx.is_connected(g):
        node = random.randrange(len(g.nodes()))
        while True:
            n = random.randrange(len(g.nodes()))
            if n != node and not g.has_edge(node, n):
                break

        g.add_edge(node, n)

    return g
