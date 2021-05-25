import numpy as np
import networkx as nx
from simulations.MonteCarlo import MonteCarlo
from pathlib import Path
import pandas as pd
from utils.plotter import plot_r_b


def save_data_iteration(results, beta, mu, name):
    path_save = f'out/simulations/monteCarlo/{name}/'
    Path(path_save).mkdir(parents=True, exist_ok=True)

    file_name = f'times_mu_{mu}_beta_{beta}.csv'

    data = pd.DataFrame.from_dict(results)
    data.to_csv(path_save + file_name)


def save_data_mu(results, mu, name):
    path_save = f'out/simulations/monteCarlo/{name}/'
    Path(path_save).mkdir(parents=True, exist_ok=True)

    file_name = f'all_mu_{mu}.csv'

    data = pd.DataFrame.from_dict(results)
    data.to_csv(path_save + file_name)


if __name__ == '__main__':
    # random_seed = 0
    # random.seed(random_seed)
    # np.random.seed(random_seed)

    graph_path = 'out/networks/tech-routers-rf.net'

    betas = np.arange(0.0, 1.02, 0.02)
    mus = [0.1, 0.5, 0.9]

    # Input
    G = nx.Graph(nx.read_pajek(graph_path))
    beta_random = 0.01
    n_rep = 1   # 50
    initial_function = 'random'
    initial_ratio = 0.1
    protection_policy = 'hubs'
    protection_ratio = 0.05
    n_max = 1000
    n_trans = 900

    title = 'simulations/monteCarlo/tech-routers-rfor.png'
    names = ['test1', 'test2']

    all_results = []

    for idx_name, mu in enumerate(mus):
        results = []
        results_csv = []

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

            print(f'Running with mu = {mu}, beta = {beta}')

            simulation_results, extended_simulation_results, _ = MC.run_simulations()

            results.append(np.mean(simulation_results))
            results_csv.append(simulation_results)

            save_data_iteration(extended_simulation_results, beta, mu, name=names[idx_name])

        save_data_mu(results_csv, mu, name=names[idx_name])

        all_results.append(results)

    plot_r_b(betas, all_results, mus, title)
