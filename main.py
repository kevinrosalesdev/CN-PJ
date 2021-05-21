import networkx as nx
import utils.read_mtx as reader
import random as rd
import src.utils.plotter as plotter

from networkgenerator import cm, er

if __name__ == '__main__':
    #k_seq = np.array(nx.utils.powerlaw_sequence(n=100, exponent=2.7))
    #k_seq = [int(k) for k in k_seq]
    #g = cm.generate_CM(k_seq)


    # This is a sample graph
    #G = er.generate_ER(50, 0.2)
    G = reader.read_mtx_file('out/networks/tech-routers-rf.mtx')

    # change the label of the nodes (just in case they have some kind of name). Transformed will be 0,1,2...
    G_abstract_name = [idx for idx in range(1, len(G.nodes) + 1)]
    labels = dict(zip(G.nodes, G_abstract_name))
    G = nx.relabel_nodes(G, labels)

    plotter.plot_network(G, title="tech-routers-rf",save=True,show=True)
    # very cutre simulator.
    historic = []
    status = [0] * len(list(G.nodes))
    p = 0.2
    iterations = 3
    #for i in range(iterations):
    #    status = [stat if rd.random()>p else 1 for stat in status]
    #    historic.append(status)
    #plotter.plot_network_status(historic, G, title='test', show=True) # it works.
