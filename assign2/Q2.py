import csv
import pandas as pd
import sys,operator

l=[]

with open("wikispeedia_paths-and-graph/categories.tsv" ,"r") as categories_f:
    for line in categories_f:
        line = line.strip()
        if(not line or line.startswith("#")):
            continue

        title, category = line.split("\t")
        
        if(category not in l):
            l.append(category)

l1=[]
l1.append('subject')
for k in l:
	cat = k.split('.')
	if(cat[0]+'.'+cat[1] not in l1):
		l1.append(cat[0]+'.'+cat[1])

l1 = sorted(l1)

d = {}
i=1
for k in l1:
	if(k not in d):
		d[k] = "C"+str(i).zfill(4)
		i=i+1

l2=[]
for k in l:
	cat = k.split('.')
	if(len(cat)>=3 and cat[0]+'.'+cat[1]+'.'+cat[2] not in l2):
		l2.append(cat[0]+'.'+cat[1]+'.'+cat[2])

l2 = sorted(l2)
for k in l2:
	if(k not in d):
		d[k] = "C"+str(i).zfill(4)
		i=i+1

l3=[]
for k in l:
	cat = k.split('.')
	if(len(cat) ==4 and cat[0]+'.'+cat[1]+'.'+cat[2]+'.'+cat[3] not in l3):
		l3.append(cat[0]+'.'+cat[1]+'.'+cat[2]+'.'+cat[3])

l3 = sorted(l3)

for k in l3:
	if(k not in d):
		d[k] = "C"+str(i).zfill(4)
		i=i+1

with open("category-ids.csv", 'w') as f:
	writer = csv.writer(f)
	for k,v in d.items():
		writer.writerow([k,v])

# df = pd.read_csv('category-ids.csv',header=None)
# df.columns = ['Category_Name','Category_ID']
# df = df.sort_values(by=['Category_Name'])
# df.to_csv('category-ids.csv' , index=False)

#sort by 1st column
data = csv.reader(open('category-ids.csv'),delimiter=',',skipinitialspace=True)
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies first column

with open("category-ids.csv", "w") as f:
  fileWriter = csv.writer(f, delimiter=',',skipinitialspace=True)
  for row in sortedlist:
      fileWriter.writerow(row)