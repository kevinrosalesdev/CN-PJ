import networkx as nx, numpy as np, random as rd
from plotter import plot_percolation


def find_gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    return G.subgraph(Gcc[0])

def find_slcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    try:
        return G.subgraph(Gcc[1])
    except:
        Exception("There is no a second largest component! (Perhaps there is only a hub of nodes"
                  "and the others are disconnected?")

def simulate_percolation(G, p:list = None):
    original_G = G.copy()
    if p is None:
        p = np.linspace(0, 1, 20)
    size_of_gcc_per_p = []
    size_of_slcc_per_p = []
    for p_value in p:
        G = original_G.copy()
        G = remove_fraction_random(G, 1-p_value)
        try:
            gcc = find_gcc(G)
            size_of_gcc_per_p.append(len(list(gcc.nodes)) / len(list(G.nodes)))
        except IndexError:
            size_of_gcc_per_p.append(0) # all nodes are disconnected.

        try:
            size_of_slcc_per_p.append(len(list(find_slcc(G))) / len(list(G.nodes)))
        except:
            size_of_slcc_per_p.append(0)
    plot_percolation(p, size_of_gcc_per_p, size_of_slcc_per_p)


def remove_fraction_random(G, p):
        # select a fraction of nodes randomly.
        number_of_nodes_to_remove = int(p*len(list(G.nodes)))
        list_of_nodes_tobe_removed = rd.sample(list(G.nodes), number_of_nodes_to_remove)

        # remove them, alongside with their adjacent edges
        G.remove_nodes_from(list_of_nodes_tobe_removed)
        return G

#find_gcc(nx.read_pajek('../../out/networks/test.net'))
#find_gcc(nx.erdos_renyi_graph(100, 0.5))
simulate_percolation(nx.read_pajek('../../out/networks/huge.net'))