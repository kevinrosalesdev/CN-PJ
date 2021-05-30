import random
import pandas as pd
import networkx as nx
import numpy as np
from utils import descriptors
import utils.read_mtx as reader
import src.utils.plotter as plotter
from strategies import strategies
from simulations.MMCA import MMCA
from networkgenerator import cm, er

if __name__ == '__main__':
    random.seed(0)


    ### Generation of Networks ###
    # k_seq = np.array(nx.utils.powerlaw_sequence(n=750, exponent=2.7))
    # k_seq = [int(k) for k in k_seq]
    # g = cm.generate_CM(k_seq)
    # plotter.plot_network(g, title="Power-Law distribution for gamma=2.7 N=750", save=True, show=False)
    # k_seq = np.array(nx.utils.powerlaw_sequence(n=1250, exponent=3.5))
    # k_seq = [int(k) for k in k_seq]
    # g = cm.generate_CM(k_seq)
    # plotter.plot_network(g, title="Power-Law distribution for gamma=3.5 N=1250", save=True, show=False)


    ### Plot of Reduced Network ###
    # G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))
    # major_nodes = [node for node, degree in dict(G.degree()).items() if degree > 2]
    # filtered_nodes = random.sample(major_nodes, int(len(major_nodes)/2))
    # G.remove_nodes_from(filtered_nodes)
    # plotter.plot_network(G, title="tech-routers-rf-lowered", save=True, show=True)


    ### Stats Extraction ###
    # graphs = [nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net')),
    #           nx.Graph(nx.read_pajek('out/networks/sf-gamma=2.7-n=750.net')),
    #           nx.Graph(nx.read_pajek('out/networks/sf-gamma=3.5-n=1250.net'))]
    # graphs_statistics = pd.DataFrame()
    # for G in graphs:
    #     d = descriptors.extract_metrics_graph(G)
    #     d = {k:[v] for k,v in d.items()}
    #     df = pd.DataFrame.from_dict(d)
    #     graphs_statistics = pd.concat([graphs_statistics, df])
    # graphs_statistics.to_csv(f'out/statistics/graphs_statistics.csv')
    # df = descriptors.extract_metrics_each_node(nx.Graph(nx.read_pajek('out/networks/sf-gamma=2.7-n=750.net')))
    # df.sort_values('column')  # sort for betweenness and degree.


    ### Histogram Extraction ###
    # G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))
    # descriptors.degree_histogram(G, log=True, title='test')


    ### MTX File Reading ###
    # G = reader.read_mtx_file('out/networks/tech-routers-rf.mtx')
    # plotter.plot_network(G, title="tech-routers-rf", save=True, show=False)


    ### Strategies ###
    # G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))
    # strategic_nodes = strategies.get_nodes(G, ratio=0.05, policy='hubs')
    # print("Nodes with Hubs Strategy:", strategic_nodes)
    # strategic_nodes = strategies.get_nodes(G, ratio=0.05, policy='betweenness')
    # print("Nodes with Betweenness Strategy:", strategic_nodes)
    # strategic_nodes = strategies.get_nodes(G, ratio=0.05, policy='mix')
    # print("Nodes with Mix Strategy:", strategic_nodes)


    ### MMCA SIS Simulation ###
    G = nx.Graph(nx.read_pajek('out/networks/tech-routers-rf.net'))
    b = np.linspace(0, 1, 51)
    mu = [0.1, 0.5, 0.9]
    protected_nodes = strategies.get_nodes(G, ratio=0.05, policy='hubs')
    mmca = MMCA(b=b, mu=mu, random_infection=0.01, rho0=0.1, t_max=500, t_trans=400)
    mean_rho_mmca = mmca.simulate(G, protected_nodes=[])
    plotter.plot_r_b(b, mean_rho_mmca, mu_list=mu, title=f"simulations/mmca-tech-routers-rf-non-protected.png")
