import pandas as pd
import csv
import networkx as nx
import operator

DG = nx.Graph()
df3 = pd.read_csv('edges.csv')

for node in range(1,4605):
	DG.add_node('A'+"{0:0=4d}".format(node))

f = open("graph-components.csv", 'w')
npath = csv.writer(f)

for row in df3.itertuples(name='Pandas'):
    DG.add_edge(row[1],row[2])

scc=[]
for t in sorted(nx.connected_components(DG),key=len,reverse=True):
	scc.append(list(t))

for sub in nx.connected_components(DG):
	H = DG.subgraph(sub).copy()
	x = nx.diameter(H)
	if(x):
		npath.writerow([len(H.nodes),nx.number_of_edges(H), x])

# con = nx.connected_components(DG)
# comps=[]
# for index,component in enumerate(con):
#     comps.append(component)
# print(len(comps))