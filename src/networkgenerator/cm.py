import networkx as nx
import random


def generate_CM(k_seq):
    k_seq = [1 if k == 0 else k for k in k_seq]     # Initial degree for all nodes must be at least 1

    if sum(k_seq) % 2 != 0:
        print("[WARNING] Total number of Stubs must be even. Adding one more stub to the first node.")
        k_seq[0] += 1

    stubs = []
    for node, k in enumerate(k_seq):
        stubs.extend([node]*k)

    random.shuffle(stubs)  # Uses the Fisher-Yates Algorithm

    g = nx.Graph()         # Multiple edges are not allowed.
    g.add_nodes_from(list(range(len(k_seq))))
    idx = 0
    while idx < len(stubs):
        g.add_edge(stubs[idx], stubs[idx+1])
        idx += 2

    g.remove_edges_from(nx.selfloop_edges(g))   # Self-loops are deleted.

    preferential_attachment = list()
    for u, v in nx.degree(g):
        preferential_attachment.extend(([u]*v))

    while not nx.is_connected(g):
        node = random.randrange(len(g.nodes()))
        while True:
            n = random.randrange(len(preferential_attachment))
            if node != preferential_attachment[n] and \
                    not g.has_edge(node, preferential_attachment[n]):
                break

        g.add_edge(node, preferential_attachment[n])

    return g
