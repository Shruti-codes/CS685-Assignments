import csv
import pandas as pd

#weekly

df1 = pd.read_csv("cases-week.csv")
df2 = pd.read_csv('neighbor-week.csv')
df4 = pd.read_csv('state-week.csv')
df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'weekid'], right_on = ['districtid', 'weekid'] )

df3 = pd.merge(df3, df4, how='left', left_on = ['districtid', 'weekid'], right_on = ['districtid', 'weekid'] )

with open("zscore-week.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['neighborstdev']==0):
			nscore = 0
		else:
			nscore = round((row['cases'] - row['neighbormean'])/row['neighborstdev'],2)

		if(row['statestdev']==0):
			sscore = 0
		else:
			sscore = round((row['cases'] - row['statemean'])/row['statestdev'],2)
		writer.writerow([int(row['districtid']), int(row['weekid']),nscore,sscore])
	f.close()

df = pd.read_csv('zscore-week.csv',header=None)
df.columns = ['districtid', 'weekid',  'neighborhoodzscore', 'statezscore']
df = df.sort_values(by=['districtid'])
df.to_csv('zscore-week.csv' , index=False)


#monthly

df1 = pd.read_csv("cases-month.csv")
df2 = pd.read_csv('neighbor-month.csv')
df4 = pd.read_csv('state-month.csv')

df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'monthid'], right_on = ['districtid', 'monthid'] )

df3 = pd.merge(df3, df4, how='left', left_on = ['districtid', 'monthid'], right_on = ['districtid', 'monthid'] )

with open("zscore-month.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['neighborstdev']==0):
			nscore = 0
		else:
			nscore = round((row['cases'] - row['neighbormean'])/row['neighborstdev'],2)

		if(row['statestdev']==0):
			sscore = 0
		else:
			sscore = round((row['cases'] - row['statemean'])/row['statestdev'],2)
		writer.writerow([int(row['districtid']), int(row['monthid']),nscore,sscore])
	f.close()

df = pd.read_csv('zscore-month.csv',header=None)
df.columns = ['districtid', 'monthid',  'neighborhoodzscore', 'statezscore']
df = df.sort_values(by=['districtid'])
df.to_csv('zscore-month.csv' , index=False)

#overall

df1 = pd.read_csv("cases-overall.csv")
df2 = pd.read_csv('neighbor-overall.csv')
df4 = pd.read_csv('state-overall.csv')
df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'timeid'], right_on = ['districtid', 'timeid'] )
df3 = pd.merge(df3, df4, how='left', left_on = ['districtid', 'timeid'], right_on = ['districtid', 'timeid'] )

with open("zscore-overall.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['neighborstdev']==0):
			nscore = 0
		else:
			nscore = round((row['cases'] - row['neighbormean'])/row['neighborstdev'],2)

		if(row['statestdev']==0):
			sscore = 0
		else:
			sscore = round((row['cases'] - row['statemean'])/row['statestdev'],2)
		writer.writerow([int(row['districtid']), int(row['timeid']),nscore,sscore])
	f.close()

df = pd.read_csv('zscore-overall.csv',header=None)
df.columns = ['districtid', 'timeid',  'neighborhoodzscore', 'statezscore']
df = df.sort_values(by=['districtid'])
df.to_csv('zscore-overall.csv' , index=False)