import random

import networkx as nx
import utils.read_mtx as reader
import src.utils.plotter as plotter

from strategies import strategies
from networkgenerator import cm, er

if __name__ == '__main__':
    random.seed(0)

    # k_seq = np.array(nx.utils.powerlaw_sequence(n=100, exponent=2.7))
    # k_seq = [int(k) for k in k_seq]
    # g = cm.generate_CM(k_seq)

    # This is a sample graph
    # G = er.generate_ER(50, 0.2)
    # G = reader.read_mtx_file('out/networks/tech-routers-rf.mtx')
    G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))

    strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='hubs')
    print("Nodes with Hubs Strategy:", strategic_nodes)
    strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='betweenness')
    print("Nodes with Betweenness Strategy:", strategic_nodes)
    strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='mix')
    print("Nodes with Mix Strategy:", strategic_nodes)

    # plotter.plot_network(G, title="tech-routers-rf", save=True, show=False)
    # plotter.plot_network_status(historic, G, title='test', show=True) # it works.
