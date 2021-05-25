import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


# array of arrays of status of each node and the nx.Graph
def plot_network_status(array_of_status_in_each_time, G, title="", show=False):
    # identify the state of each node and create two partitions of the graph: S and I. Plot with different colors
    # the partitions.
    # index of the status -> index of the node
    for idx, array_of_status in enumerate(array_of_status_in_each_time):
        color_map = []
        for node in array_of_status:
            if node == 0: # node susceptible
                color_map.append('blue')
            elif node == 1: # node infected
                color_map.append('red')
            elif node == 2: # state: 2 - node recovered
                color_map.append('green')
            else:
                color_map.append('black') # state: 3 - protected
        nx.draw(G, node_color=color_map, with_labels=True)
        plt.savefig(f"out/networks_states/STATUS-(t={idx})-{title}.png")
        if show:
            plt.show()


# plots the fraction of infected nodes in the network at each time. (Montecarlo with several realizations)
def plot_r_t(t_max: int, rho: list, b: list, title, show=False):
    plt.clf()
    rho = rho[0]
    # The structure of the tensor should be: [p(t0) p(t1)...] para b0-> <p> -> [<p>(b0) <p>(b1)...] ->
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
    if show:
        plt.show()


def plot_r_b(b, rho, mu_list, title="", show=False):
    plt.clf()
    # generate a plot for each mu.
    for idx in range(len(rho)):
        plt.plot(b, rho[idx], '-o', label=f"MC-μ={mu_list[idx]}")

    # create figure.
    plt.title(title)
    plt.xlabel('β')
    plt.ylabel('ρ')
    plt.legend()
    plt.title(title)
    plt.savefig(f"out/{title}")
    if show:
        plt.show()


def plot_network(g, title='', width=0.1, node_size=10, save=True, show=False):
    plt.clf()
    plt.title(title)
    pos = nx.kamada_kawai_layout(g, weight=None)
    nx.draw(g, pos, node_size=node_size, width=width)

    if show:
        plt.show()
    if save:
        plt.savefig(f"out/networks-plots/{title}.png")
        #nx.write_pajek(g, f'out/networks/{title}.net')


def plot_percolation(p, size_of_gcc_record, size_of_slcc_record, title='', show=False):
    plt.clf()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(p, size_of_gcc_record, '-o')
    ax1.set_ylabel('gcc')
    ax1.set_xlabel('p')

    ax2 = ax1.twinx()
    ax2.plot(p, size_of_slcc_record, 'grey', alpha=0.8)
    ax2.set_ylabel('slcc')
    for tl in ax2.get_yticklabels():
        tl.set_color('black')

    plt.title(title)
    # plt.plot(p, size_of_gcc_record, '-o')
    # plt.plot(p, size_of_slcc_record, '-x')
    plt.xlabel('p')
    # plt.ylabel('GCC')
    #plt.legend(['GCC', 'SLCC'])
    # plt.savefig(f"out/{title}")
    plt.savefig(f"out/percolation_graphs/{title}.png")
    if show: plt.show()


def plot_histogram(hist:dict , title = 'Degree Histogram', show=False):
    # format the bins and x axis of the plot
    minim,maxim = min(hist.keys()), max(hist.keys())
    x = range(minim, maxim+1)
    plt.xticks(x, x)

    # plot
    plt.bar(hist.keys(), hist.values(), width=1, color='g', edgecolor='black')
    # further parameters
    plt.title(title)
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig(f"out/degree-histograms/{title}.png")
    if show: plt.show()


