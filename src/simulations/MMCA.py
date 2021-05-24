import random
import numpy as np


# Ratio of infected nodes
def _get_rho(prob):
    return np.sum(prob)/len(prob)


def _get_healthy_neighbors_ratio(g, prob, idx_node_i):
    neighbors_state = [1 if prob[int(neighbor)] < 0.5 else 0 for neighbor in g.neighbors(str(idx_node_i))]
    return np.sum(neighbors_state)/len(neighbors_state)


class MMCA:

    def __init__(self, b, mu, random_infection: float = 0.01, rho0: float = 0.1, t_max: int = 500, t_trans: int = 400):
        self.b = b
        self.mu = mu
        self.rho0 = rho0
        self.t_max = t_max
        self.t_trans = t_trans
        self.random_infection = random_infection

    def simulate(self, g, protected_nodes):
        self.protected_nodes = np.array(protected_nodes, dtype=int)
        mean_rho_mmca = []
        for mu in self.mu:
            mean_rho_mmca.append(self._simulate_mu(g, mu))
        return mean_rho_mmca

    def _simulate_mu(self, g, mu_value):
        mean_rho_per_beta = []
        initial_prob = np.array([self.rho0]*len(g.nodes()))
        initial_prob[self.protected_nodes] = 0
        rho_history_bvalue = []
        for b_idx, b_value in enumerate(self.b):
            beta_protected_nodes = self.protected_nodes.copy()
            print(f"Step: {b_idx+1}/{len(self.b)}")
            prob = initial_prob.copy()
            rho_history = [_get_rho(prob)]
            for step in range(1, self.t_max):
                old_prob = prob.copy()
                prob = np.array([(1 - old_prob[idx])*(1 - self._q_node(g, b_idx, old_prob, idx))
                                 + ((1-(mu_value*_get_healthy_neighbors_ratio(g, old_prob, idx))) * old_prob[idx])
                                for idx in range(len(old_prob))])
                prob = np.array([1.0 if random.random() < self.random_infection else prob_value for prob_value in prob])
                prob[beta_protected_nodes] = 0
                # beta_protected_nodes = np.unique(np.concatenate((beta_protected_nodes, np.where(prob < 0.1)[0])))
                rho_history.append(_get_rho(prob))
            rho_history_bvalue.append(rho_history)

        # Transitory state is discarded.
        for rho_one_beta_realization in rho_history_bvalue:
            mean_rho_per_beta.append(np.mean(rho_one_beta_realization[self.t_trans:], axis=0))

        return mean_rho_per_beta

    # Probability that a node is not infected by any neighbor.
    def _q_node(self, g, b_idx, prob, idx_node_i):
        pr_noinfection_each_neighbor = [1-(self.b[b_idx]*prob[int(neighbor)])
                                        for neighbor in g.neighbors(str(idx_node_i))]
        return np.prod(np.array(pr_noinfection_each_neighbor))
