import random

import networkx as nx
import numpy as np

import utils.read_mtx as reader
import src.utils.plotter as plotter

from strategies import strategies
from simulations.MMCA import MMCA
from networkgenerator import cm, er

if __name__ == '__main__':
    random.seed(0)

    # k_seq = np.array(nx.utils.powerlaw_sequence(n=100, exponent=2.7))
    # k_seq = [int(k) for k in k_seq]
    # g = cm.generate_CM(k_seq)

    # This is a sample graph
    # G = er.generate_ER(50, 0.2)
    # G = reader.read_mtx_file('out/networks/tech-routers-rf.mtx')
    # plotter.plot_network(G, title="tech-routers-rf", save=True, show=False)
    G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))

    b = np.linspace(0, 1, 51)
    mu = [0.1, 0.5, 0.9]
    protected_nodes = strategies.get_nodes(G, ratio=0.05, policy='hubs')
    mmca = MMCA(b=b, mu=mu, random_infection=0.01, rho0=0.1, t_max=500, t_trans=400)
    mean_rho_mmca = mmca.simulate(G, protected_nodes=[])
    plotter.plot_r_b(b, mean_rho_mmca, mu_list=mu, title=f"simulations/mmca-tech-routers-rf-non-protected.png")

    # strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='hubs')
    # print("Nodes with Hubs Strategy:", strategic_nodes)
    # strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='betweenness')
    # print("Nodes with Betweenness Strategy:", strategic_nodes)
    # strategic_nodes = strategies.get_nodes(G, ratio=0.01, policy='mix')
    # print("Nodes with Mix Strategy:", strategic_nodes)

    # plotter.plot_network_status(historic, G, title='test', show=True) # it works.
