import pandas as pd
import csv
import sys,operator
from collections import defaultdict
import networkx as nx

p = pd.read_csv("wikispeedia_paths-and-graph/paths_finished.tsv" ,sep='\t', skiprows=15, header=None,names=['hashedIpAddress','timestamp','durationInSec','path','rating'])
path = p.iloc[:,3:4]	#finished paths 

art_cat = defaultdict(list)
myFile = open ("article-categories.csv","r")
archive = csv.reader(myFile, delimiter=',')
for rows in archive:
	art_cat[rows[0]] = (rows[1:])

art = pd.read_csv("article-ids.csv", header=None, index_col=0, squeeze=True).to_dict()


DG = nx.DiGraph()
for node_num in range(1,4605):
	DG.add_node('A'+"{0:0=4d}".format(node_num))

df3 = pd.read_csv('edges.csv')
for row in df3.itertuples(name='Pandas'):
    DG.add_edge(row[1],row[2])

path_visited = {}

def findShortPath(pair):
    source = pair.split(',')[0]
    target = pair.split(',')[1]
    try:
        _ = nx.shortest_path(DG, source=source, target=target)
        # print(_)
        path_visited[pair] = _
        
    except:
        print('')

cl = [0]*147	#no of categories
clp = [0]*147	#no of paths

f = open("category-paths.csv", 'w')
npath = csv.writer(f)

def remove_back(path):
	stack =[]
	for el in path:
		if(el!='<'):
			stack.append(el)
		else:
			stack.pop()

	return stack

for row in path.itertuples(name='Pandas'):
	clb = [False]*147
	# b = row[1].count 
	# s=""
	# s1 = row[1].split(';')
	# if(b):
	# 	for i in range(len(s1)):
	# 		if(not s):
	# 			s = s1[i] + ';'
	# 		else:
	# 			s = s+ ';'+ s1[i]
			
	# 		if(s1[i]=='<'):
	# 			ind = s[:s.rfind(";")].rfind(";")
	# 			s =  s[:ind]

	# if(not s):
	# 	s=row[1]
	
	# s=""
	sub = remove_back(row[1].split(';'))
	# sub = s.join(st)
	# print(sub)
	s= ';'.join(sub)
	sub = str(s).split(';')	#articles in one path
	source = art[sub[0]]
	target = art[sub[len(sub)-1]]
	pair = source+','+target
	findShortPath(pair)
	# c=[]
	if(len(sub)>1):
		for x in sub:
			# if(x in art.keys()):
			aid = art[x]	#get article id of article in path
			if(aid in art_cat.keys()):
				# c = art_cat[aid]		#get categories of that article
				for cx in art_cat[aid]:
					i = int(cx[1:])
					cl[i]+=1; #number of times this category comes

					if(clb[i]==False):	#to just visit cat once in a path
						clb[i] = True
						clp[i]+=1		#if this cat is visited in this path or not

#shortest paths
scl = [0]*147	#no of categories
sclp = [0]*147	#no of paths

for row in path.itertuples(name='Pandas'):
	sclb = [False]*147
	sub = str(row[1]).split(';')	#articles in one path
	source = art[sub[0]]
	target = art[sub[len(sub)-1]]
	pair = source+','+target #start and end node

	if(pair in path_visited.keys()):
		x = path_visited[pair]	#shortest path route for that pair
		for cx in x:		#for every article in route
			for cxx in art_cat[cx]:		#for category of that article
				i = int(cxx[1:])
				scl[i]+=1; #number of times this category comes

				if(sclb[i]==False):	#to just visit cat once in a path
					sclb[i] = True
					sclp[i]+=1		#if this cat is visited in this path or not

for i in range(1,len(cl)):
	npath.writerow(["C"+str(i).zfill(4), clp[i], cl[i],sclp[i], scl[i]])

# df = pd.read_csv('category-paths.csv',header=None)
# df.columns = ['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed']
# df = df.sort_values(by=['Category_ID'])
# df.to_csv('category-paths.csv' , index=False)