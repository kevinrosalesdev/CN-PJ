import numpy as np
import networkx as nx
from simulations import initialState
from strategies import strategies


class MonteCarlo:

    def __init__(self,
                 G: nx.Graph,
                 beta: float,
                 beta_random: float,
                 mu: float,
                 n_rep: int = 50,
                 inital_fnc: str = 'random',
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

        protected = strategies.get_nodes(self.G, self.protection_ratio, self.protection_policy)

        for rep in range(self.n_rep):
            if rep % 10 == 0:
                print(f'Rep: {rep}')

            simulation_output = self.single_simulation(protected)
            # Maximum Rho of the iterations(b)
            simulation_results.append(simulation_output)

        # np.average(Maximum Rho of the iterations)(b) [50 values -> 1 per beta]

        return simulation_results

    def single_simulation(self, protected: list):
        '''
        Run a single execution of a SIR model and returns both the infection rate and the status of the nodes for each iteration
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

        for i in range(self.n_max):
            # If iteration is over -> No infected nodes left
            if np.count_nonzero(node_status == 1) == 0:
                # Exit iteration for -> as no infected node so no possible changes
                break

            for idx_node in range(n):

                # If node is susceptible:
                if node_status[idx_node] == 0:
                    # Contamination by random
                    aux = np.random.rand(1) < self.beta_random

                    if aux == 1:
                        next_node_status[idx_node] = 1
                    else:
                        # Contamination by neighbors
                        idx_neighbors = [int(x) for x in list(self.G.neighbors(str(idx_node)))]
                        nbr_infected_neighbors = np.count_nonzero(node_status[idx_neighbors] == 1)
                        next_node_status[idx_node] = np.any(np.random.rand(nbr_infected_neighbors) < self.beta)

                # If node is infected
                elif node_status[idx_node] == 1:
                    # Recovery depending on neighbors
                    # If random number < self.mu -> Node has recovered -> New status = 2 (1+1)
                    # If random number > self.mu -> Node has not recovered and is still infected -> Status still 1 (0+1)
                    idx_neighbors = [int(x) for x in list(self.G.neighbors(str(idx_node)))]
                    # Healthy neighbors are the number of neighbors minus the ones infected
                    num_healthy_neighbors = len(idx_neighbors) - np.count_nonzero(node_status[idx_neighbors] == 1)
                    ratio_healthy_neighbors = num_healthy_neighbors / len(idx_neighbors)

                    next_node_status[idx_node] = (np.random.rand(1) < self.mu * ratio_healthy_neighbors) + 1

                # If node is recovery
                # elif node_status[idx_node] == 2:

                # If node is protected
                # elif node_status[idx_node] == 3:

            # Update node_status
            node_status = next_node_status

        # Computer number of recovered nodes of final state:
        output = np.count_nonzero(node_status == 2) / n
        return output
