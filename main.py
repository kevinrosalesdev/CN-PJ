import networkx as nx
import numpy as np

from networkgenerator import cm

if __name__ == '__main__':
    k_seq = np.array(nx.utils.powerlaw_sequence(n=100, exponent=2.7))
    k_seq = [int(k) for k in k_seq]
    g = cm.generate_CM(k_seq)