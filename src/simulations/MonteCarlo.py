import numpy as np
import networkx as nx
import initialState
import strategies


class monteCarlo:

    def __init__(self,
                 G: nx.Graph,
                 beta: float,
                 beta_random: float,
                 mu: float,
                 n_rep: int = 50,
                 inital_fnc: str = 'default',
                 initial_ratio: float = 0.1,
                 protection_policy: str = 'hubs',
                 protection_ratio: float = 0.1,
                 n_max: int = 1000,
                 n_trans: int = 900):
        self.G = G
        self.beta = beta
        self.beta_random = beta_random
        self.mu = mu
        self.n_rep = n_rep
        self.n_max = n_max
        self.n_trans = n_trans

        self.initial_fnc = inital_fnc
        self.initial_ratio = initial_ratio
        self.protection_policy = protection_policy
        self.protection_ratio = protection_ratio


    def run_simulations(self):
        simulation_results = []
        time_fracs = {}







    def compute_spreading(self, protected: list):
        '''
        Run a single execution of a SIR model and returns
        Node states options:
        0 -> Susceptible
        1 -> Infected
        2 -> Recovered
        3 -> Protected
        :return:
        '''
        n = self.G.number_of_nodes()
        node_status = initialState.get_initial_state(n, protected, ratio=self.initial_ratio, policy=self.initial_fnc)
        next_node_status = node_status.copy()

        output = []

        for i in range(self.n_max):
            for idx_node in range(n):
                # If node is susceptible:
                if node_status[idx_node] == 0:
                    # Contamination by random
                    aux = np.random.rand(1) < self.beta_random

                    if aux == 1:
                        next_node_status[idx_node] = 1
                    else:
                        # Contamination by neighbors
                        idx_neighbors = list(self.G.neighbors(idx_node))
                        nbr_infected_neighbors = np.count_nonzero(node_status[idx_neighbors] == 1)
                        next_node_status[idx_node] = np.any(np.random.rand(nbr_infected_neighbors) < self.beta)

                # If node is infected
                elif node_status[idx_node] == 1:
                    # Recovery
                    next_node_status[idx_node] = 2 * node_status * (np.random.rand(1) > self.mu)

                # If node is recovery
                # elif node_status[idx_node] == 2:

                # If node is protected
                # elif node_status[idx_node] == 3:

            # Save information iteration & update node_status
            node_status = next_node_status
            output.append(np.count_nonzero(node_status == 1) / n)

        return output