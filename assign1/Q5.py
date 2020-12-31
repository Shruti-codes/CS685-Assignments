import json
import csv
import pandas as pd
from datetime import timedelta
import datetime as dt
import numpy as np

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

others = ['other state' , 'others', 'other region', 'unassigned', 'unknown']
common = ["aurangabad", "balrampur", "bilaspur", "hamirpur", "pratapgarh"]

start = dt.datetime(2020,3,15)
end = dt.datetime(2020,9,5)

#weekly

df = pd.read_csv('data.csv')
df3 = pd.read_csv('cases-week.csv')

date=start
w=1

with open('state-week.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	while(date.date()<=end.date()):
		date = start + timedelta(days=7)
		wbegin = start
		df1 = pd.DataFrame()
		
		#extracting weekly information together
		while(wbegin<date):
			i = df['date'] == str(wbegin.date())
			wbegin=wbegin+timedelta(days=1)
			df1 = df1.append(df[i])

		l = df1['state'].unique()
		
		for s in l:
			df2 = pd.DataFrame()
			j = df1['state'] == s	#find other districts of same state in that time frame
			df2 = df1[j]			#contains districts of same state only
			d={}
			l2 = df2['district'].unique()
			
			for dis in l2:
				n=dis.lower()	#take one district
				s_code = s.lower()

				if(len(l2)==1):
					if(l2[0].lower()=='unknown'):
						for key, value in data.items():	#find id of that district
							if(key==("unknown_"+s.lower())):
								idd1 = value['id']
								break
					else:
						for key, value in data.items():		#find id
							sub = key.split("/")
							if(sub[0]==n):
								idd1 = value['id']
								break
					writer.writerow([idd1,w,0,0])
					continue
				
				flag = 0
				if(n in common):
					flag = 1
					if(n == common[0]):
						if(s_code == "br"):
							idd1 = data["aurangabad/Q43086"]['id']
						elif(s_code == 'mh'):
							idd1 = data["aurangabad/Q592942"]['id']
				
					elif(n == common[1]):
						if(s_code == 'ct'):
							idd1 = data["balrampur/Q16056268"]['id']
						elif(s_code == 'up'):
							idd1 = data["balrampur/Q1948380"]['id']
				
					elif(n == common[2]):
						if(s_code == 'ct'):
							idd1 = data["bilaspur/Q100157"]['id']
						elif(s_code == 'hp'):
							idd1 = data["bilaspur/Q1478939"]['id']
				
					elif(n == common[3]):
						if(s_code == 'up'):
							idd1 = data["hamirpur/Q2019757"]['id']
						elif(s_code == 'hp'):
							idd1 = data["hamirpur/Q2086180"]['id']
				
					elif(n == common[4]):
						if(s_code == "up"):
							idd1 = data["pratapgarh/Q1473962"]['id']
						elif(s_code == 'rj'):
							idd1 = data["pratapgarh/Q1585433"]['id']

				if(flag==0):
					for key, value in data.items():	#find id of that district
						sub = key.split("/")
						if(sub[0]==n):
							idd1 = value['id']
							break

				c1 = df3.loc[((df3['districtid']==idd1) & (df3['weekid']==w)) ,'cases']	#find cases for that week
				try:
					c1 = c1.values[0]
				except IndexError:
					continue

				if(idd1 not in d.keys()):
					d[idd1] = {'id': idd1, 'w': w ,'m1':c1, 'm2': [] }
				else:
					continue

				for dis1 in l2:		#traversing all other districts of same state
					n1 = dis1.lower()

					flag = 0
					if(n1 in common):
						flag = 1
						if(n1 == common[0]):
							if(s_code == "br"):
								idd = data["aurangabad/Q43086"]['id']
							elif(s_code == 'mh'):
								idd = data["aurangabad/Q592942"]['id']
					
						elif(n1 == common[1]):
							if(s_code == 'ct'):
								idd = data["balrampur/Q16056268"]['id']
							elif(s_code == 'up'):
								idd = data["balrampur/Q1948380"]['id']
					
						elif(n1 == common[2]):
							if(s_code == 'ct'):
								idd = data["bilaspur/Q100157"]['id']
							elif(s_code == 'hp'):
								idd = data["bilaspur/Q1478939"]['id']
					
						elif(n1 == common[3]):
							if(s_code == 'up'):
								idd = data["hamirpur/Q2019757"]['id']
							elif(s_code == 'hp'):
								idd = data["hamirpur/Q2086180"]['id']
					
						elif(n1 == common[4]):
							if(s_code == "up"):
								idd = data["pratapgarh/Q1473962"]['id']
							elif(s_code == 'rj'):
								idd = data["pratapgarh/Q1585433"]['id']

					if(flag==0):
						for key, value in data.items():		#find id
							sub = key.split("/")
							if(sub[0]==n1):
								idd = value['id']
								break

					c = df3.loc[ ((df3['districtid']==idd) & (df3['weekid']==w)) ]['cases']	#find cases for that week
					try:
						c = c.values[0]
					except IndexError:
						continue 
						
					if(n1!=n and idd1 in d.keys()):
						d[idd1]['m2'].append(c)
						d[idd1] = {'id': idd1, 'w':w ,'m1': d[idd1]['m1'] ,'m2':d[idd1]['m2'] }

			for k1,v1 in d.items():
				m = round(np.mean(v1['m2']),2)
				st = round(np.std(v1['m2']), 2)
				writer.writerow([v1['id'],v1['w'],m,st])

		start = date
		w+=1
	f.close()

df = pd.read_csv('state-week.csv',header=None)
df.columns = ['districtid', 'weekid', 'statemean', 'statestdev']
df = df.sort_values(by=['districtid'])
df.to_csv('state-week.csv' , index=False)

#monthly
df = pd.read_csv('data.csv')
df3 = pd.read_csv('cases-month.csv')

start = dt.datetime(2020,3,15)
end = dt.datetime(2020,9,5)

def get_next_month(date):
    month = (date.month%12)+1
    year = date.year + (date.month + 1 > 12)
    return dt.datetime(year, month, 1)

date = dt.datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S')
m=1
with open('state-month.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	while(date.date()<=end.date()):
		date = get_next_month(start)
		wbegin = start
		df1 = pd.DataFrame()
		
		#extracting monthly information together
		while(wbegin<date and wbegin<=end):
			i = df['date'] == str(wbegin.date())
			wbegin=wbegin+timedelta(days=1)
			df1 = df1.append(df[i])

		l = df1['state'].unique()
		
		for s in l:
			d={}
			df2 = pd.DataFrame()
			j = df1['state'] == s	#find other districts of same state in that time frame
			df2 = df1[j]			#contains districts of same state only
			l2 = df2['district'].unique()
			for dis in l2:
				n=dis.lower()	#take one district
				s_code = s.lower()

				if(len(l2)==1):
					if(l2[0].lower()=='unknown'):
						for key, value in data.items():	#find id of that district
							if(key==("unknown_"+s.lower())):
								idd1 = value['id']
								break
					else:
						for key, value in data.items():		#find id
							sub = key.split("/")
							if(sub[0]==n):
								idd1 = value['id']
								break
					writer.writerow([idd1,m,0,0])
					continue
				
				flag = 0
				if(n in common):
					flag = 1
					if(n == common[0]):
						if(s_code == "br"):
							idd1 = data["aurangabad/Q43086"]['id']
						elif(s_code == 'mh'):
							idd1 = data["aurangabad/Q592942"]['id']
				
					elif(n == common[1]):
						if(s_code == 'ct'):
							idd1 = data["balrampur/Q16056268"]['id']
						elif(s_code == 'up'):
							idd1 = data["balrampur/Q1948380"]['id']
				
					elif(n == common[2]):
						if(s_code == 'ct'):
							idd1 = data["bilaspur/Q100157"]['id']
						elif(s_code == 'hp'):
							idd1 = data["bilaspur/Q1478939"]['id']
				
					elif(n == common[3]):
						if(s_code == 'up'):
							idd1 = data["hamirpur/Q2019757"]['id']
						elif(s_code == 'hp'):
							idd1 = data["hamirpur/Q2086180"]['id']
				
					elif(n == common[4]):
						if(s_code == "up"):
							idd1 = data["pratapgarh/Q1473962"]['id']
						elif(s_code == 'rj'):
							idd1 = data["pratapgarh/Q1585433"]['id']

				if(flag==0):
					for key, value in data.items():	#find id of that district
						sub = key.split("/")
						if(sub[0]==n):
							idd1 = value['id']
							break
				
				c1 = df3.loc[((df3['districtid']==idd1) & (df3['monthid']==m)) , 'cases']	#find cases for that month
				try:
					c1 = c1.values[0]
				except IndexError:
					continue

				if(idd1 not in d.keys()):
					d[idd1] = {'id': idd1, 'm': m ,'m1':c1, 'm2': [] }
				else:
					continue

				for dis1 in l2:		#traversing all other districts of same state
					n1 = dis1.lower()
					flag = 0
					if(n1 in common):
						flag = 1
						if(n1 == common[0]):
							if(s_code == "br"):
								idd = data["aurangabad/Q43086"]['id']
							elif(s_code == 'mh'):
								idd = data["aurangabad/Q592942"]['id']
					
						elif(n1 == common[1]):
							if(s_code == 'ct'):
								idd = data["balrampur/Q16056268"]['id']
							elif(s_code == 'up'):
								idd = data["balrampur/Q1948380"]['id']
					
						elif(n1 == common[2]):
							if(s_code == 'ct'):
								idd = data["bilaspur/Q100157"]['id']
							elif(s_code == 'hp'):
								idd = data["bilaspur/Q1478939"]['id']
					
						elif(n1 == common[3]):
							if(s_code == 'up'):
								idd = data["hamirpur/Q2019757"]['id']
							elif(s_code == 'hp'):
								idd = data["hamirpur/Q2086180"]['id']
					
						elif(n1 == common[4]):
							if(s_code == "up"):
								idd = data["pratapgarh/Q1473962"]['id']
							elif(s_code == 'rj'):
								idd = data["pratapgarh/Q1585433"]['id']

					if(flag==0):
						for key, value in data.items():		#find id
							sub = key.split("/")
							if(sub[0]==n1):
								idd = value['id']
								break

					c = df3.loc[ ((df3['districtid']==idd) & (df3['monthid']==m)), 'cases']#find cases for that month
					try:
						c = c.values[0]
					except IndexError:
						continue 
						
					if(n1!=n and idd1 in d.keys()):
						d[idd1]['m2'].append(c)
						d[idd1] = {'id': idd1, 'm': m ,'m1': d[idd1]['m1'] ,'m2':d[idd1]['m2'] }

			for k1,v1 in d.items():
				me = round(np.mean(v1['m2']),2)
				st = round(np.std(v1['m2']), 2)
				writer.writerow([v1['id'],v1['m'],me,st])

		start = date
		m+=1
	f.close()


df = pd.read_csv('state-month.csv',header=None)
df.columns = ['districtid', 'monthid', 'statemean', 'statestdev']
df = df.sort_values(by=['districtid'])
df.to_csv('state-month.csv' , index=False)


#overall
df = pd.read_csv('data.csv')
df3 = pd.read_csv('cases-overall.csv')

with open('state-overall.csv', 'w', newline='') as f:
	writer = csv.writer(f)

	l = df['state'].unique()

	for s in l:
		d={}
		df2 = pd.DataFrame()
		j = df['state'] == s	#find other districts of same state in that time frame
		df2 = df[j]				#contains districts of same state only
		l2 = df2['district'].unique()

		for dis in l2:
			n=dis.lower()						#take one district
			s_code = s.lower()

			if(len(l2)==1):
					if(l2[0].lower()=='unknown'):
						for key, value in data.items():	#find id of that district
							if(key==("unknown_"+s.lower())):
								idd1 = value['id']
								break
					else:
						for key, value in data.items():		#find id
							sub = key.split("/")
							if(sub[0]==n):
								idd1 = value['id']
								break
					writer.writerow([idd1,1,0,0])
					continue
				
			flag = 0
			if(n in common):
				flag = 1
				if(n == common[0]):
					if(s_code == "br"):
						idd1 = data["aurangabad/Q43086"]['id']
					elif(s_code == 'mh'):
						idd1 = data["aurangabad/Q592942"]['id']
				
				elif(n == common[1]):
					if(s_code == 'ct'):
						idd1 = data["balrampur/Q16056268"]['id']
					elif(s_code == 'up'):
						idd1 = data["balrampur/Q1948380"]['id']
				
				elif(n == common[2]):
					if(s_code == 'ct'):
						idd1 = data["bilaspur/Q100157"]['id']
					elif(s_code == 'hp'):
						idd1 = data["bilaspur/Q1478939"]['id']
				
				elif(n == common[3]):
					if(s_code == 'up'):
						idd1 = data["hamirpur/Q2019757"]['id']
					elif(s_code == 'hp'):
						idd1 = data["hamirpur/Q2086180"]['id']
				
				elif(n == common[4]):
					if(s_code == "up"):
						idd1 = data["pratapgarh/Q1473962"]['id']
					elif(s_code == 'rj'):
						idd1 = data["pratapgarh/Q1585433"]['id']

			if(flag==0):
				for key, value in data.items():	#find id of that district
					sub = key.split("/")
					if(sub[0]==n):
						idd1 = value['id']
						break

			if(flag==0):
				for key, value in data.items():		#find id of that district
					sub = key.split("/")
					if(sub[0]==n):
						idd1 = value['id']
						break

			c1 = df3.loc[(df3['districtid']==idd1) ,'cases']	#find overall cases for that district
			try:
				c1 = c1.values[0]
			except IndexError:
				continue

			if(idd1 not in d.keys()):
				d[idd1] = {'id': idd1, 'm1':c1, 'm2': [] }
			else:
				continue

			for dis1 in l2:		#traversing all other districts of same state
				n1 = dis1.lower()
				flag = 0
				if(n1 in common):
					flag = 1
					if(n1 == common[0]):
						if(s_code == "br"):
							idd = data["aurangabad/Q43086"]['id']
						elif(s_code == 'mh'):
							idd = data["aurangabad/Q592942"]['id']
					
					elif(n1 == common[1]):
						if(s_code == 'ct'):
							idd = data["balrampur/Q16056268"]['id']
						elif(s_code == 'up'):
							idd = data["balrampur/Q1948380"]['id']
					
					elif(n1 == common[2]):
						if(s_code == 'ct'):
							idd = data["bilaspur/Q100157"]['id']
						elif(s_code == 'hp'):
							idd = data["bilaspur/Q1478939"]['id']
					
					elif(n1 == common[3]):
						if(s_code == 'up'):
							idd = data["hamirpur/Q2019757"]['id']
						elif(s_code == 'hp'):
							idd = data["hamirpur/Q2086180"]['id']
					
					elif(n1 == common[4]):
						if(s_code == "up"):
							idd = data["pratapgarh/Q1473962"]['id']
						elif(s_code == 'rj'):
							idd = data["pratapgarh/Q1585433"]['id']

				if(flag==0):
					for key, value in data.items():		#find id
						sub = key.split("/")
						if(sub[0]==n1):
							idd = value['id']
							break

				c = df3.loc[ (df3['districtid']==idd),'cases']		#find overall cases for that id
				try:
					c = c.values[0]
				except IndexError:
					continue 
						
				if(n1!=n and idd1 in d.keys()):
					d[idd1]['m2'].append(c)
					d[idd1] = {'id': idd1, 'm1': d[idd1]['m1'] ,'m2':d[idd1]['m2'] }

			for k1,v1 in d.items():
				me = round(np.mean(v1['m2']),2)
				st = round(np.std(v1['m2']), 2)
				writer.writerow([v1['id'],1,me,st])

	f.close()

df = pd.read_csv('state-overall.csv',header=None)
df.drop_duplicates(subset = None,inplace=True)
df.to_csv('state-overall.csv' , index=False)

df = pd.read_csv('state-overall.csv',header=None)
df.columns = ['districtid', 'timeid', 'statemean', 'statestdev']
df = df.sort_values(by=['districtid'])
df.to_csv('state-overall.csv' , index=False)
