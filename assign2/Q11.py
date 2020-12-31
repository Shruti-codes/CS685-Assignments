from collections import defaultdict
import csv
import pandas as pd
import urllib.parse

csv_file = open("wikispeedia_paths-and-graph/paths_finished.tsv",encoding='utf-8')
paths = csv.reader(csv_file)
lis=[]
for row in paths:
    if len(row)>0 and row[0][0]!='#':
        lis.append(row)

df1=pd.read_csv('category-pairs.csv')
fromcat=df1.iloc[0].tolist()
tocat=df1.iloc[1].tolist()

df1=pd.read_csv("finished-paths-no-back.csv")

source_des=[]
for row in lis:
    row=row[0].split('\t')[3].split(';')
    source=urllib.parse.unquote(row[0])
    dest=urllib.parse.unquote(row[-1])
    source_des.append([source,dest])

art_cat = defaultdict(list)
myFile = open ("article-categories.csv","r")
archive = csv.reader(myFile, delimiter=',')

for rows in archive:
	art_cat[rows[0]] = (rows[1:])
art = pd.read_csv("article-ids.csv",index_col=0, squeeze=True).to_dict()

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

dicratio={}
diccnt={}
for index,row in df1.iterrows():
    ratio= row[2]
    entry=source_des[index]
    source_art=entry[0]
    dest_art=entry[1]

    if(source_art in art.keys() and dest_art in art.keys()):
	    scid=art_cat[art[source_art]]		#category of source
	    tcid=art_cat[art[dest_art]]
	    
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

	    for pair in li:
	    	if(pair not in dicratio.keys()):
	    		dicratio[pair] = ratio
	    		diccnt[pair] = 1
	    	else:
	    		dicratio[pair]+=ratio
	    		diccnt[pair]+=1

avgratio={}
for k,v in dicratio.items():
    avgratio[k]=dicratio[k]/diccnt[k]

# print(len(avgratio.keys()))

df2=pd.DataFrame(avgratio.items(),columns=['Category','Ratio_of_human_to_shortest'])
df2=df2.sort_values(by=['Category'])
df4=pd.DataFrame()
df4[['From_Category','To_Category']]=df2.Category.str.split(',',expand=True)
df2=df2.drop(['Category'],axis=1)
df5=pd.concat([df4,df2],axis=1)

df5.to_csv('category-ratios.csv',index=False,encoding='utf8')