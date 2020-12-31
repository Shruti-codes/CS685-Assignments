import csv
from collections import defaultdict
import pandas as pd
import sys,operator

art = pd.read_csv("article-ids.csv", index_col=0, squeeze=True).to_dict()
cat = pd.read_csv("category-ids.csv", header=None, index_col=0, squeeze=True).to_dict()
temp=[]
article_categories = defaultdict(list)

with open("wikispeedia_paths-and-graph/categories.tsv" ,"r") as categories_f:
    for line in categories_f:
        line = line.strip()
        if(not line or line.startswith("#")):
            continue

        title, category = line.split("\t")
        article_id = art[title]
        temp.append(article_id)

        category_id = cat[category]
        if(category_id not in article_categories[article_id]):
        	article_categories[article_id].append(category_id)

#for articles with missing categories
for k, v in art.items():
    if(v not in temp):
        category_id = cat['subject']
        article_categories[v].append(category_id)

with open("article-categories.csv", 'w',newline='') as f:
	writer = csv.writer(f)
	for k,v in article_categories.items():
		writer.writerow([k]+v)

#sort by 1st column
data = csv.reader(open('article-categories.csv'),delimiter=',',skipinitialspace=True)
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies first column

with open("article-categories.csv", "w") as f:
  fileWriter = csv.writer(f, delimiter=',',skipinitialspace=True)
  for row in sortedlist:
      fileWriter.writerow(row)

    


        


