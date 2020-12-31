import pandas as pd
import csv
import sys,operator

p = pd.read_csv("wikispeedia_paths-and-graph/paths_finished.tsv" ,sep='\t', skiprows=15, header=None)
spath = pd.read_csv("wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt" , skiprows=17, header=None)
art = pd.read_csv("article-ids.csv", index_col=0, squeeze=True).to_dict()
art_list = list(art)

f = open("finished-paths-no-back.csv",'w')
npath = csv.writer(f)

f2 = open("finished-paths-back.csv",'w')
npath2 = csv.writer(f2)

#fourth column
path = p.iloc[:,3:4]
for row in path.itertuples(name='Pandas'):
	b = row[1].count('<')
	s = row[1].replace('<','')
	
	sub = str(s).split(';')
	hdist = (len(sub)-1) - b*2
	hdist2 = len(sub)-1
	
	if(sub[0] in art_list and sub[len(sub)-1] in art_list):
		a1 = art_list.index(sub[0]) #first
		a2 = art_list.index(sub[len(sub)-1]) #last

	# d = spath.iloc[a1]
		for line in spath.iloc[a1]:
			if(line[a2]!='_' and line[a2]!='0'):
				sdist = line[a2]
				npath.writerow([hdist, sdist, round(hdist/int(sdist),2)])
				npath2.writerow([hdist2, sdist, round(hdist2/int(sdist),2)])
				break

#sort by 1st column
# data = csv.reader(open('finished-paths-no-back.csv'),delimiter=',',skipinitialspace=True)
# sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies first column

# with open("finished-paths-no-back.csv", "w") as f:
#   fileWriter = csv.writer(f, delimiter=',',skipinitialspace=True)
#   for row in sortedlist:
#       fileWriter.writerow(row)

# #sort by 1st column
# data = csv.reader(open('finished-paths-back.csv'),delimiter=',',skipinitialspace=True)
# sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies first column

# with open("finished-paths-back.csv", "w") as f:
#   fileWriter = csv.writer(f, delimiter=',',skipinitialspace=True)
#   for row in sortedlist:
#       fileWriter.writerow(row)