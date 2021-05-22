import numpy as np
import networkx as nx
import random

def get_initial_state(number_nodes: int, protected: list, ratio: float = 0.1,  policy: str = 'random'):
    '''
    Returns the initial state of the nodes given the chosen policy and ration
    :param number_nodes: number of nodes in the graph
    :param protected: List of indexes which nodes are protected
    :param ratio: Ratio for the given policy if required
    :param policy:
        -   'random': Randomly selects ratio*N nodes to be initially hacked
    :return: an array with the initial status of each node of the graph
    '''
    initial_state = np.zeros(number_nodes)
    initial_state[protected] = 3

    idx = np.array(list(range(number_nodes)))
    idx_possible = np.delete(idx, protected)

    if policy == 'random':
        idx_infected = random.sample(list(idx_possible), int(number_nodes * ratio))
        initial_state[idx_infected] = 1
    elif policy == 'none':
        pass
    else:
        raise Exception(f"Policy {policy} is not included. Please, use 'random' or 'none'")

    return initial_state