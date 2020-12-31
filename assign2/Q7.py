import pandas as pd
import csv

fp = pd.read_csv("finished-paths-no-back.csv", index_col=0)
fpb = pd.read_csv("finished-paths-back.csv", index_col=0)

f = open("percentage-paths-no-back.csv", 'w')
npath = csv.writer(f,quoting=csv.QUOTE_NONE,escapechar=' ')

h0=0
h=[0]*11
h1=0
c=0

for row in fp.itertuples(name='Pandas'):
	c=c+1
	x = int(row[0]-row[1])
	if(x==0):
		h0 =h0+1

	elif(x>=1 and x<=10):
		h[x] = h[x] + 1

	else:
		h1=h1+1

l=[(x/c)*100 for x in h[1:]]
s=",".join(map(str,l))
npath.writerow([(h0/c)*100,s,(h1/c)*100])

f2 = open("percentage-paths-back.csv", 'w')
npath2 = csv.writer(f2,quoting=csv.QUOTE_NONE,escapechar=' ')

h0=0
h=[0]*11
h1=0
c=0

for row in fpb.itertuples(name='Pandas'):
	c=c+1
	x = row[0] - row[1]
	if(x==0):
		h0 =h0+1

	elif(x>=1 and x<=10):
		h[x] = h[x] + 1

	else:
		h1=h1+1

l=[(x/c)*100 for x in h[1:]]
s=",".join(map(str,l))
npath2.writerow([(h0/c)*100,s,(h1/c)*100])


