import random
import networkx as nx

from igraph import read
from os import remove
from networkx import Graph


def read_mtx_file(filename: str) -> Graph:
	# preprocess the file. Remove the two first lines of the header as they are for 
	# explanatory purposes only (not part of the graph!!!). THIS ONLY WORKS WITH MTX FILES FROM
	# networkrepository.com
	with open(filename, 'r') as fin:
		data = fin.read().splitlines(True)
	with open(f'{filename}_clean.mtx', 'w') as fout:
		fout.writelines(data[2:])

	# read the code in igraph, since this library can read clean mtx files.
	g = read(f'{filename}_clean.mtx', format="edge")

	# clean all generated files (they were transitory)
	remove(f'{filename}_clean.mtx')

	# removes empty node (iGraph expects a "node 0")
	g.delete_vertices([0])

	# returns a networkx graph.
	g = nx.Graph(g.to_networkx().to_undirected())

	# remove self-loops
	g.remove_edges_from(nx.selfloop_edges(g))

	# change the label of the nodes (just in case they have some kind of name). Transformed will be 0,1,2...
	G_abstract_name = [idx for idx in range(1, len(g.nodes) + 1)]
	labels = dict(zip(g.nodes, G_abstract_name))
	g = nx.relabel_nodes(g, labels)

	# ensures that the network is fully connected using preferential attachment.
	preferential_attachment = list()
	for u, v in nx.degree(g):
		preferential_attachment.extend(([u]*v))

	while not nx.is_connected(g):
		node = random.randrange(len(g.nodes()))
		while True:
			n = random.randrange(len(preferential_attachment))
			if node != preferential_attachment[n] and \
					not g.has_edge(node, preferential_attachment[n]):
				break

		g.add_edge(node, preferential_attachment[n])

	return g
	
# uncomment for debugging purposes.

#nx.write_pajek(read_mtx_file("176bit.mtx"), f'../../out/networks/huge.net')
