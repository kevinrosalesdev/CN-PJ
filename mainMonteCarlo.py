import numpy as np
import networkx as nx
from simulations.MonteCarlo import MonteCarlo
from pathlib import Path
import pandas as pd
from utils.plotter import plot_r_b


def save_results(dir_path: str, name: str, results_to_save):
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    data = pd.DataFrame.from_dict(results_to_save)
    data.to_csv(dir_path + name + '.csv', index=False)


if __name__ == '__main__':
    # random_seed = 0
    # random.seed(random_seed)
    # np.random.seed(random_seed)

    # 'out/networks/Power-Law-distribution-for-gamma=2.7-N=750.net'
    # 'out/networks/Power-Law distribution for gamma=3.5 N=1250.net'
    # 'out/networks/tech-routers-rf.net'
    graph_path = 'out/networks/tech-routers-rf.net'
    network_file_name = 'tech-routers-rf'

    # Input
    G = nx.Graph(nx.read_pajek(graph_path))
    beta_random = 0.0
    n_rep = 50
    initial_function = 'random'
    initial_ratio = 0.1
    # protection_policy = 'mix'
    # protection_ratio = 0.1
    n_max = 500
    n_trans = 0

    protection_policies = ['hubs', 'betweenness', 'mix']
    protected_ratios = [0.05, 0.1, 0.2]
    mus = [0.1, 0.5, 0.9]
    betas = np.arange(0.0, 1.02, 0.02)

    for protection_policy in protection_policies:
        for protection_ratio in protected_ratios:

            results_all_mu = []

            for mu in mus:
                results = []
                extended_results = []

                for beta in betas:
                    MC = MonteCarlo(
                        G=G,
                        beta=beta,
                        beta_random=beta_random,
                        mu=mu,
                        n_rep=n_rep,
                        inital_fnc=initial_function,
                        initial_ratio=initial_ratio,
                        protection_policy=protection_policy,
                        protection_ratio=protection_ratio,
                        n_max=n_max,
                        n_trans=n_trans,
                    )

                    print(
                        f'Running with protection policy {protection_policy}, protected ratio = {protection_ratio}, mu = {mu}, beta = {beta}')

                    simulation_results = MC.run_simulations()
                    results.append(np.mean(simulation_results))
                    extended_results.append(simulation_results)

                prefix_save = f'out/simulations/monteCarlo/{network_file_name}/{protection_policy}/pr_{protection_ratio}/mu_{mu}/'

                # Save results and append to results all mu
                save_results(prefix_save, 'results', results)
                save_results(prefix_save, 'extended_results', extended_results)
                results_all_mu.append(results)

            title = f'simulations/monteCarlo/{network_file_name}/{protection_policy}/{network_file_name}_pr{protection_ratio}.png'
            plot_r_b(betas, results_all_mu, mus, title)
