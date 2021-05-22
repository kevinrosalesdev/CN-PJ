import networkx as nx


def get_nodes(g: nx.Graph, ratio: float = 0.1, policy: str = 'hubs'):
    """
    Returns ratio*num_nodes(G) nodes based on the applied policy.

    :param g: Graph
    :param ratio: Ratio of total number of nodes to return (default=0.1)
    :param policy:
        - 'hubs': return N hubs (N nodes with more degree in G)
        - 'betweenness': return N nodes with more betweenness in G
        - 'mix': return N/2 hubs and N/2 nodes with more betweenness in G.
    :return: appropriate nodes based on the policy.
    """
    n_nodes = int(ratio*len(g.nodes()))
    nodes = []
    if policy == 'hubs':
        degree = [(node, degree) for node, degree in nx.degree(g)]
        degree.sort(key=lambda x: x[1], reverse=True)
        for node in range(n_nodes):
            nodes.append(degree[node][0])
    elif policy == 'betweenness':
        betweenness = [(node, betweenness) for node, betweenness in nx.betweenness_centrality(g).items()]
        betweenness.sort(key=lambda x: x[1], reverse=True)
        for node in range(n_nodes):
            nodes.append(betweenness[node][0])
    elif policy == 'mix':
        degree = [(node, degree) for node, degree in nx.degree(g)]
        degree.sort(key=lambda x: x[1], reverse=True)
        betweenness = [(node, betweenness) for node, betweenness in nx.betweenness_centrality(g).items()]
        betweenness.sort(key=lambda x: x[1], reverse=True)
        node = 0
        while len(nodes) < n_nodes:
            if degree[node][0] not in nodes:
                nodes.append(degree[node][0])
            if betweenness[node][0] not in nodes:
                nodes.append(betweenness[node][0])
            node += 1
    else:
        raise Exception(f"Policy {policy} is not included. Please, use 'hubs', 'betweenness' or 'mix'")
    return nodes
