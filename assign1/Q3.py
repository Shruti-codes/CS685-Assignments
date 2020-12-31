import json
import csv
from collections import defaultdict

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

#generating district edge graphs
# Q3
with open('edge-graph.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for k, v in data.items():
		for x in v['neighbors']:
			if(data[k]["id"] < data[x]["id"]):
				li=[]
				li.extend([data[k]['id'], data[x]['id']])
				writer.writerow(li)
	f.close()