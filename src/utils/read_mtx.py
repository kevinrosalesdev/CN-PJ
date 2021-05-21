from igraph import read
from os import remove
from networkx import Graph


def read_mtx_file(filename:str, keep_directed = False) -> Graph:
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
	
	# returns a networkx graph.
	if keep_directed:
		return g.to_networkx()
	return g.to_networkx().to_undirected()
	
# uncomment for debugging purposes.
#read_mtx_file("test.mtx")
