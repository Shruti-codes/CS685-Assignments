import csv
import pandas as pd

titles = []
with open("wikispeedia_paths-and-graph/articles.tsv", 'r') as f:
	for row in f:
		row = row.strip()
		if(not row or row.startswith("#")):
			continue
		titles.append(row) 

art_dict = {}
i=1
for x in titles:
	art_dict[x] = "A"+str(i).zfill(4)
	i=i+1

with open("article-ids.csv", 'w') as f:
	writer = csv.writer(f)
	for k,v in art_dict.items():
		writer.writerow([k,v])

df = pd.read_csv('article-ids.csv',header=None)
df.columns = ['Article_Name','Article_ID']
df = df.sort_values(by=['Article_Name'])
df.to_csv('article-ids.csv' , index=False)