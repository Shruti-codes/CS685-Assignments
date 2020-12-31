import csv
import pandas as pd

#weekly

df1 = pd.read_csv("cases-week.csv")
df2 = pd.read_csv('neighbor-week.csv')
df4 = pd.read_csv('state-week.csv')

df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'weekid'], right_on = ['districtid', 'weekid'] )
df5 = pd.merge(df1, df4, how='left', left_on = ['districtid', 'weekid'], right_on = ['districtid', 'weekid'] )

with open("method-spot-week.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['cases']>(row['neighbormean']+row['neighborstdev'])):
			writer.writerow([ int(row['weekid']),'neighborhood','hot',int(row['districtid'])])
		elif(row['cases']<(row['neighbormean']-row['neighborstdev'])):
			writer.writerow([ int(row['weekid']),'neighborhood','cold', int(row['districtid'])])

	for ind, row in df5.iterrows():
		if(row['cases']>(row['statemean']+row['statestdev'])):
			writer.writerow([ int(row['weekid']),'state','hot',int(row['districtid'])])
		elif(row['cases']<(row['statemean']-row['statestdev'])):
			writer.writerow([ int(row['weekid']),'state','cold', int(row['districtid'])])
	f.close()

df = pd.read_csv('method-spot-week.csv',header=None)
df.columns = ['weekid', 'method', 'spot', 'districtid']
df = df.sort_values(by=['weekid'])
df.to_csv('method-spot-week.csv' , index=False)

#monthly

df1 = pd.read_csv("cases-month.csv")
df2 = pd.read_csv('neighbor-month.csv')
df4 = pd.read_csv('state-month.csv')

df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'monthid'], right_on = ['districtid', 'monthid'] )
df5 = pd.merge(df1, df4, how='left', left_on = ['districtid', 'monthid'], right_on = ['districtid', 'monthid'] )

with open("method-spot-month.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['cases']>(row['neighbormean']+row['neighborstdev'])):
			writer.writerow([ int(row['monthid']),'neighborhood','hot',int(row['districtid'])])
		elif(row['cases']<(row['neighbormean']-row['neighborstdev'])):
			writer.writerow([ int(row['monthid']),'neighborhood','cold', int(row['districtid'])])

	for ind, row in df5.iterrows():
		if(row['cases']>(row['statemean']+row['statestdev'])):
			writer.writerow([ int(row['monthid']),'state','hot',int(row['districtid'])])
		elif(row['cases']<(row['statemean']-row['statestdev'])):
			writer.writerow([ int(row['monthid']),'state','cold', int(row['districtid'])])
	f.close()

df = pd.read_csv('method-spot-month.csv',header=None)
df.columns = ['monthid', 'method', 'spot', 'districtid']
df = df.sort_values(by=['monthid'])
df.to_csv('method-spot-month.csv' , index=False)


#overall
df1 = pd.read_csv("cases-overall.csv")
df2 = pd.read_csv('neighbor-overall.csv')
df4 = pd.read_csv('state-overall.csv')

df1['districtid'] = df1['districtid'].astype(int)
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'timeid'], right_on = ['districtid', 'timeid'] )
df5 = pd.merge(df1, df4, how='left', left_on = ['districtid', 'timeid'], right_on = ['districtid', 'timeid'] )

with open("method-spot-overall.csv", 'w', newline = '') as f:
	writer = csv.writer(f)
	for ind, row in df3.iterrows():
		if(row['cases']>(row['neighbormean']+row['neighborstdev'])):
			writer.writerow([ int(row['timeid']),'neighborhood','hot',int(row['districtid'])])
		elif(row['cases']<(row['neighbormean']-row['neighborstdev'])):
			writer.writerow([ int(row['timeid']),'neighborhood','cold', int(row['districtid'])])

	for ind, row in df5.iterrows():
		if(row['cases']>(row['statemean']+row['statestdev'])):
			writer.writerow([ int(row['timeid']),'state','hot',int(row['districtid'])])
		elif(row['cases']<(row['statemean']-row['statestdev'])):
			writer.writerow([ int(row['timeid']),'state','cold', int(row['districtid'])])
	f.close()

df = pd.read_csv('method-spot-overall.csv',header=None)
df.columns = ['timeid', 'method', 'spot', 'districtid']
df = df.sort_values(by=['timeid'])
df.to_csv('method-spot-overall.csv' , index=False)