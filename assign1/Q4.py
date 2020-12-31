import csv
import pandas as pd
import json
import numpy as np

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

#weekly
df1 = pd.read_csv("cases-week.csv")

with open('neighbor-week.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for ind in df1.index:
		d={}
		df2 = df1.loc[df1['weekid']==df1.loc[ind,'weekid']]

		for key, value in data.items():
			if(df1.loc[ind,'districtid']==data[key]['id']):
				for x in value['neighbors']:
					for i in df2.index:
						if(df2.loc[i,'districtid']==data[x]['id']):
							if(df1.loc[ind,'districtid'] not in d.keys()):
								d[df1.loc[ind,'districtid']] = { 'id': df1.loc[ind,'districtid'], 'w': df1.loc[ind,'weekid'], 'm1': df1.loc[ind,'cases'], 'm2': [df2.loc[i,'cases']]}
							else:
								d[df1.loc[ind,'districtid']]['m2'].append(df2.loc[i,'cases'])
								d[df1.loc[ind,'districtid']] = { 'id': df1.loc[ind,'districtid'], 'w': df1.loc[ind,'weekid'],'m1': df1.loc[ind,'cases'], 'm2': d[df1.loc[ind,'districtid']]['m2'] }
				
				break
		
		for k,v in d.items():
			m = round(np.mean(v['m2']),2)
			s = round(np.std(v['m2']), 2)
			writer.writerow([v['id'],v['w'],m,s])

	f.close()

df = pd.read_csv('neighbor-week.csv',header=None)
df.columns = ['districtid', 'weekid', 'neighbormean', 'neighborstdev']
df = df.sort_values(by=['districtid'])
df.to_csv('neighbor-week.csv' , index=False)


#monthly
df1 = pd.read_csv("cases-month.csv")

with open('neighbor-month.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for ind in df1.index:
		d={}
		df2 = df1.loc[df1['monthid']==df1.loc[ind,'monthid']]

		for key, value in data.items():
			if(df1.loc[ind,'districtid']==data[key]['id']):
				for x in value['neighbors']:
					for i in df2.index:
						if(df2.loc[i,'districtid']==data[x]['id']):
							if(df1.loc[ind,'districtid'] not in d.keys()):
								d[df1.loc[ind,'districtid']] = { 'id': df1.loc[ind,'districtid'], 'm': df1.loc[ind,'monthid'], 'm1': df1.loc[ind,'cases'], 'm2': [df2.loc[i,'cases']]}
							else:
								d[df1.loc[ind,'districtid']]['m2'].append(df2.loc[i,'cases'])
								d[df1.loc[ind,'districtid']] = {'id':df1.loc[ind,'districtid'], 'm': df1.loc[ind,'monthid'],'m1':df1.loc[ind,'cases'], 'm2': d[df1.loc[ind,'districtid']]['m2']}


				break

		for k,v in d.items():
			m = round(np.mean(v['m2']),2)
			s = round(np.std( v['m2']), 2)
			writer.writerow([v['id'],v['m'],m,s])

	f.close()

df = pd.read_csv('neighbor-month.csv',header=None)
df.columns = ['districtid', 'monthid', 'neighbormean', 'neighborstdev']
df = df.sort_values(by=['districtid'])
df.to_csv('neighbor-month.csv' , index=False)


# #overall
df1 = pd.read_csv("cases-overall.csv")

with open('neighbor-overall.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for ind in df1.index:
		d={}
		df2 = df1.loc[df1['timeid']==df1.loc[ind,'timeid']]

		for key, value in data.items():
			if(df1.loc[ind,'districtid']==data[key]['id']):
				for x in value['neighbors']:
					for i in df2.index:
						if(df2.loc[i,'districtid']==data[x]['id']):
							if(df1.loc[ind,'districtid'] not in d.keys()):
								d[df1.loc[ind,'districtid']] = {'id': df1.loc[ind,'districtid'], 'o': df1.loc[ind,'timeid'], 'm1':df1.loc[ind,'cases'], 'm2': [df2.loc[i,'cases']]}
							else:
								d[df1.loc[ind,'districtid']]['m2'].append(df2.loc[i,'cases'])
								d[df1.loc[ind,'districtid']] = { 'id':df1.loc[ind,'districtid'], 'o':df1.loc[ind,'timeid'],'m1':df1.loc[ind,'cases'], 'm2': d[df1.loc[ind,'districtid']]['m2']}


				break

		for k,v in d.items():
			m = round(np.mean( v['m2']),2)
			s = round(np.std( v['m2']), 2)
			writer.writerow([v['id'],v['o'],m,s])

	f.close()

df = pd.read_csv('neighbor-overall.csv',header=None)
df.columns = ['districtid', 'timeid', 'neighbormean', 'neighborstdev']
df = df.sort_values(by=['districtid'])
df.to_csv('neighbor-overall.csv' , index=False)