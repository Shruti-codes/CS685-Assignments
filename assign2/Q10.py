import pandas as pd
import csv
from collections import defaultdict
import sys,operator
import collections

p = pd.read_csv("wikispeedia_paths-and-graph/paths_unfinished.tsv" ,sep='\t', skiprows=17, header=None)
cid = pd.read_csv("category-ids.csv", header=None, index_col=0, squeeze=True).to_dict()

l=[]
lid = []
for row,v in cid.items():
	l.append(row)
	lid.append(v)

cat_dict = defaultdict(list)	#dict of subcat parents
for x in l:
	for y in l:
		if(x.startswith(y) and len(x)>=len(y) and x!=y):
			cat_dict[cid[x]].append(cid[y])

# print(cat_dict)

art_cat = defaultdict(list)
myFile = open ("article-categories.csv","r")
archive = csv.reader(myFile, delimiter=',',skipinitialspace=True)

for rows in archive:
	art_cat[rows[0]] = (rows[1:])

art = pd.read_csv("article-ids.csv",index_col=0, squeeze=True).to_dict()
#Long_peper
#Adolph_Hitler
#Podcast
#Sportacus
#Charlottes_web
#Macedonia - Macedon
#_Zebra - Zebra
#Western_Australia - Australia
#Bogota - Bogot
#Kashmir - Kashmir_region

d=defaultdict(int)

for row in p.itertuples(name='Pandas'):
	source = row[4].split(';')[0]
	target = row[5]

	art['Test'] = 'X0001'
	art_cat['X0001'] = 'C0001'
	art['Netbook'] = 'X0002'
	art_cat['X0002'] = 'C0001'
	art['Podcast'] = art['Podcasting']
	art['Christmas'] = art['A_Christmas_Carol']
	art['C++'] = 'X0003'
	art_cat['X0003'] ='C0001'
	art['Usa'] = 'X0004'
	art_cat['X0004'] ='C0001'
	art['Rss'] = 'X0005'
	art_cat['X0005'] ='C0001'
	art['Black_ops_2'] = 'X0006'
	art_cat['X0006'] ='C0001'
	art['The_Rock'] = 'X0007'
	art_cat['X0007'] ='C0001'
	art['Great'] = 'X0008'
	art_cat['X0008'] ='C0001'
	art['Georgia'] = 'X0009'
	art_cat['X0009'] ='C0001'
	art['English'] = 'X0010'
	art_cat['X0010'] ='C0001'
	art['Fats'] = 'X0011'
	art_cat['X0011'] ='C0001'
	art['Mustard'] = 'X0012'
	art_cat['X0012'] ='C0001'
	art['The'] = 'X0013'
	art_cat['X0013'] ='C0001'
	art['Rat'] = 'X0014'
	art_cat['X0014'] ='C0001'

	said = art[source]	#get articleid of source
	taid = art[target]
	scid = art_cat[said]	#get categoryid of source
	tcid = art_cat[taid]

	sscid = []
	for x in range(len(scid)):
		sscid.append(scid[x])
		temp = cat_dict[scid[x]]
		for y in temp:
			sscid.append(y)

	stcid = []
	for x in range(len(tcid)):
		stcid.append(tcid[x])
		temp = cat_dict[tcid[x]]
		for y in temp:
			stcid.append(y)

	
	li=set()
	for y in range(len(sscid)): #for all subcat
		for z in range(len(stcid)):
			pair=sscid[y]+','+stcid[z]
			li.add(pair)

	for el in li:
		d[el]+=1
	
p = pd.read_csv("wikispeedia_paths-and-graph/paths_finished.tsv" ,sep='\t', skiprows=17, header=None)
path = p.iloc[:,3:4]	#finished paths 
d2 = defaultdict(int)
for row in path.itertuples(name='Pandas'):
	sub = str(row[1]).split(';')	#articles in one path
	source = art[sub[0]]
	target = art[sub[len(sub)-1]]

	scid = art_cat[source]
	tcid = art_cat[target]

	sscid = []
	for x in range(len(scid)):
		sscid.append(scid[x])
		temp = cat_dict[scid[x]]
		for y in temp:
			sscid.append(y)

	stcid = []
	for x in range(len(tcid)):
		stcid.append(tcid[x])
		temp = cat_dict[tcid[x]]
		for y in temp:
			stcid.append(y)

	li=set()
	for y in range(len(sscid)): #for all subcat
		for z in range(len(stcid)):
			pair=sscid[y]+','+stcid[z]
			li.add(pair)

	for el in li:
		d2[el]+=1

# print(len(set(d.keys()) - set(d2.keys())))
# print(d2.keys())

d = collections.OrderedDict(sorted(d.items()))
d2 = collections.OrderedDict(sorted(d2.items()))

f = open("category-pairs.csv", 'w', newline='')
npath = csv.writer(f)

for k, pf in d2.items():
	if(k in d.keys()):
		puf = d[k]
		sub = k.split(',')
		npath.writerow([sub[0],sub[1],(pf/(pf+puf))*100,(puf/(pf+puf))*100])
	else:
		sub = k.split(',')
		npath.writerow([sub[0],sub[1],pf,0])

for k, v in d.items():
	if(k not in d2.keys()):
		puf = d[k]
		sub = k.split(',')
		npath.writerow([sub[0],sub[1],0,puf])

# df = pd.read_csv('category-pairs.csv',header=None)
# df.columns = ['From_Category','To_Category','Percentage_of_finished_paths','Percentage_of_unfinished_paths']
# df = df.sort_values(by=['From_Category'])
# df.to_csv('category-pairs.csv' , index=False)