import networkx as nx, pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from utils.plotter import plot_histogram

'''Returns a dictionary {degree:occurrences} for each degree available
in the graph. If specified, plots the histogram.'''


def degree_histogram(G, plot=False, log=True, title='') -> dict:
    degree_histogram = {}
    for node_deg in G.degree:
        degree = node_deg[1]
        degree_histogram[degree] = degree_histogram.get(degree, 0) + 1
    # cut for linear
    if not log: degree_histogram = {k: v for k, v in degree_histogram.items() if k < 10}
    if log:
        k = [degree for degree in degree_histogram.values()]
        nbins = 10
        k_log = np.log10(k)
        k_min_log = np.log10(np.min(k))
        k_max_log = np.log10(np.max(k) + 1)
        intervals = np.linspace(k_min_log, k_max_log, nbins + 1)
        freq_k_log = [np.where((intervals[i] <= k_log) & (k_log < intervals[i + 1]))[0].shape[0]
                      for i in range(nbins)]
        p_b = np.divide(freq_k_log, len(k))
        x = [(intervals[i] + intervals[i + 1]) / 2 for i in range(len(intervals) - 1)]
        plt.bar(x, p_b, width=x[1] - x[0], log=log, edgecolor='black')
        plt.xticks(x, [round(i, 2) for i in x])
        plt.title(title)
        plt.xlabel('Degree')
        plt.ylabel('Frequency (log)')
        if plot: plt.show()
        plt.savefig(f"out/degree-histograms/{title}.png")

    else:
        plot_histogram(degree_histogram, show=plot, title=title)
    return degree_histogram


'''Returns a pandas dataframe with the metrics and statistics of each node. Results are rounded as indicated in
float_depth'''


def extract_metrics_each_node(G, float_depth=4) -> pd.DataFrame():
    G = nx.Graph(G)
    df = pd.DataFrame(columns=['avg_degree',
                               'avg_clustering', 'max_path_length', 'avg_path_length',
                               'betweenness', 'eigenvec_centra', 'pagerank'])
    degree = get_degree(G, float_depth)
    cc = get_clustering_coefficient(G)
    betweenness = get_betweenness(G)
    eigenvec_cent = get_eigenvector_centrality(G)
    pagerank = get_pagerank(G)
    dist_info = get_distances(G)

    for index, node in enumerate(G.nodes):
        df.loc[index] = {'avg_degree': round(degree['avg'], float_depth),
                         'avg_clustering': round(cc[node], float_depth),
                         'max_path_length': [tupl[1] for tupl in dist_info if node in tupl][0],
                         'avg_path_length': round([tupl[2] for tupl in dist_info if node in tupl][0], float_depth),
                         'betweenness': round(betweenness[node], float_depth),
                         'eigenvec_centra': round(eigenvec_cent[node], float_depth),
                         'pagerank': round(pagerank[node], float_depth)}
    return df


def extract_metrics_graph(G, float_depth=4) -> dict:
    keys = ['nodes', 'edges', 'min_degree', 'max_degree', 'avg_degree', 'avg_clustering', 'assortativity',
            'avg_path_length', 'diameter']

    G = nx.Graph(G)  # multigraph to simple undirected graph, otherwise some metrics will not work.
    statistics = {k: 0 for k in keys}

    degree = get_degree(G, float_depth)
    statistics['nodes'] = get_nodes_number(G)
    statistics['edges'] = get_edges_number(G)
    statistics['min_degree'] = degree['min']
    statistics['max_degree'] = degree['max']
    statistics['avg_degree'] = degree['avg']
    statistics['avg_clustering'] = get_average_clustering(G, float_depth)
    statistics['assortativity'] = get_assortativity(G, float_depth)
    statistics['avg_path_length'] = get_average_path_length(G, float_depth)
    statistics['diameter'] = get_diameter(G, float_depth)

    return statistics


def get_nodes_number(graph):
    return nx.number_of_nodes(graph)


def get_edges_number(graph):
    return nx.number_of_edges(graph)


# degree of a node is number of edges connected to it
def get_degree(graph, float_depth):
    degrees = [val for (node, val) in nx.degree(graph)]
    return {"min": np.min(degrees),
            "max": np.max(degrees),
            "avg": round(np.mean(degrees), float_depth)}


# clustering coefficient of a node measures how much interconnected
# it is with its neighbours. C = connections / connections if clique
def get_average_clustering(graph, float_depth):
    return round(nx.average_clustering(graph), 10)


# the preference of the network's nodes to attach to others that are similar
# to them in some way (typ~node's degree)
def get_assortativity(graph, float_depth):
    return round(nx.degree_assortativity_coefficient(graph), float_depth)


#  avg number of steps along the shortest paths calculated over all pair of nodes
# measures the efficiency of information.
def get_average_path_length(graph, float_depth):
    return round(nx.average_shortest_path_length(graph), float_depth)


# length of the longest shortest path between any two nodes.
def get_diameter(graph, float_depth):
    return round(nx.diameter(graph), float_depth)


def get_clustering_coefficient(graph):
    return nx.clustering(graph, weight=None)


def get_betweenness(graph):
    return nx.betweenness_centrality(graph, weight=None)


# centrality of a node based on the centrality of its neighbors. If M is the adjency matrix of the graph,
# we compute the eigenvalues and vectors of that matrix.
def get_eigenvector_centrality(graph):
    return nx.eigenvector_centrality(graph, weight=None)


# ranking of the nodes in the graph G based on the structure of the incoming links.
# It was originally designed as an algorithm to rank web pages
def get_pagerank(graph):
    return nx.pagerank(graph, weight=None)


# returns a dictionary of dictionaries. Key: name of airport and value, which is a dictionary with key airport value
# distance with the first key.
def get_distances(graph):
    path_info_dict = dict(nx.all_pairs_shortest_path_length(graph))
    node_statistics = []
    for node in path_info_dict:
        max_path_length = max((path_info_dict[node].values()))
        distance_metrics = list(path_info_dict[node].values())
        avg_path_length = np.mean(distance_metrics)
        node_statistics.append((node, max_path_length, avg_path_length))
    return node_statistics

######################################################################################
# uncomment for debugging purposes
# _ = degree_histogram(nx.read_pajek('../../out/networks/tech-routers-rf.net'), plot=True, log=False)
# a = extract_metrics(nx.read_pajek('../../out/networks/test.net').to_undirected())
# a = extract_metrics_graph(nx.read_pajek('../../out/networks/huge.net'))
# print()
