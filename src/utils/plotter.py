import networkx as nx
from matplotlib import pyplot as plt


# array of arrays of status of each node and the nx.Graph
def plot_network_status(array_of_status_in_each_time, G, title="", show=False):
    # identify the state of each node and create two partitions of the graph: S and I. Plot with different colors
    # the partitions.
    # index of the status -> index of the node
    for idx, array_of_status in enumerate(array_of_status_in_each_time):
        color_map = []
        for node in array_of_status:
            if node == 0:
                color_map.append('blue')
            else:
                color_map.append('red')
        nx.draw(G, node_color=color_map, with_labels=True)
        plt.savefig(f"out/networks_states/STATUS-(t={idx})-{title}.png")
        if show: plt.show()

    pass


# plots the fraction of infected nodes in the network at each time. (Montecarlo with several realizations)
def plot_r_t(t_max: int, rho:list, b:list, title, show=False):
    plt.clf()
    rho = rho[0] # The structure of the tensor should be: [p(t0) p(t1)...] para b0-> <p> -> [<p>(b0) <p>(b1)...] ->
                 # (fin montecarlo) -> [[<p>(b0)...](m0) [<p>(b0)...](m1)...]. Para una sola mu sin promediado temporal,
                 # quedaría [[p(t0) p(t1)...](b0)  [p(t0) p(t1)...](b1) ...](m0)
    t = list(range(t_max))
    for idx in range(len(b)):
        plt.plot(t, rho[idx])

    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('ρ')
    plt.legend([f"β={b_value}" for b_value in b])
    plt.savefig(f"out/{title}")
    if show: plt.show()


def plot_r_b(b, rho_MC, mu_list, title="", show=False):
    plt.clf()
    # generate a plot for each mu.
    for idx in range(len(rho_MC)):
        plt.plot(b, rho_MC[idx], '-o', label=f"MC-μ={mu_list[idx]}")

    # create figure.
    plt.title(title)
    plt.xlabel('β')
    plt.ylabel('ρ')
    plt.legend()
    plt.title(title)
    plt.savefig(f"out/{title}")
    if show: plt.show()


def plot_network(g, title='', width=0.1, node_size=10, save=True, show=False):
    plt.clf()
    plt.title(title)
    pos = nx.kamada_kawai_layout(g, weight=None)
    nx.draw(g, pos,  node_size=node_size, width=width)

    if show: plt.show()
    if save:
        plt.savefig(f"out/networks-plots/{title}.png")
        nx.write_pajek(g, f'out/networks/{title}.net')
