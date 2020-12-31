#coding: utf-8
import json
import csv
import pandas as pd
from collections import defaultdict
from datetime import timedelta
import datetime as dt

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

others = ['other state' , 'others', 'other region', 'unassigned', 'unknown']
leave = ['Airport Quarantine', 'BSF Camp', 'Evacuees', 'Foreign Evacuees', 'Gaurela Pendra Marwahi', 'Hnahthial', 
'Italians', 'Khawzawl', 'Railway Quarantine', 'Ranipet', 'Saitual', 'Tenkasi', 'Tirupathur', 'Vijayapura', 'Yanam']
common = ["aurangabad", "balrampur", "bilaspur", "hamirpur", "pratapgarh"]
state_code = ['as', 'mn', 'ga', 'tg', 'sk']

f = open('data-all.json')
data = json.load(f)
f.close()

f = open("data.csv", 'w', newline='')
writer = csv.writer(f)
l=[]
for key, value in data.items():
	for k, v in value.items():
		for k1, v1 in v.items():
			if(k1=='districts'):
				for k2, v2 in v1.items():
					l.extend([key,k,k2])
					try:
						l.append(data[key][k][k1][k2]['delta']['confirmed'])
						l.append('delta')
					except KeyError:
						try:
							l.append(data[key][k][k1][k2]['total']['confirmed'])
							l.append('total')
						except KeyError:
							l.clear()
							continue
					if(len(l)>0):
						writer.writerow(l)
						l.clear()

f.close()

df=pd.read_csv('data.csv')
df.columns = ['date','state', 'district', 'confirmed','tag']
df.to_csv('data.csv',  index=False)
df = pd.read_csv('data.csv')

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

# weekly cases district wise

start = dt.datetime(2020,3,15)
end = dt.datetime(2020,9,5)
date=start
w=1
with open('cases-week.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	while(date.date()<=end.date()):
		date = start + timedelta(days=7)
		wbegin = start
		d = {}
		df1 = pd.DataFrame()

		while(wbegin<date):
			i = df['date'] == str(wbegin.date())
			df1 = df1.append(df[i])
			wbegin=wbegin+timedelta(days=1)
		
		for ind in df1.index:
			dis = df1.loc[ind,'district'].lower()
			s_code = df1.loc[ind,'state'].lower()

			if(s_code in state_code and dis in others):
				
				if((dis+"_"+s_code) not in d.keys()):
					d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c': df1.loc[ind,'confirmed']}
				else:
					if(df1.loc[ind,'tag']=='delta'):
						d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c':d[dis+'_'+s_code]['c']+df1.loc[ind,'confirmed']}
					elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
						d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c':df1.loc[ind,'confirmed']-d[dis+'_'+s_code]['c']}
				

			if(dis in common):
				
				if(dis == common[0]):
					if(s_code == "br"):
						if((dis+"_"+s_code) not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':df1.loc[ind,'confirmed']-d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'mh'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c': df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
				elif(dis == common[1]):
					if(s_code == 'ct'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c': df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'up'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
				
				
				elif(dis == common[2]):
					if(s_code == 'ct'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

					elif(s_code == 'hp'):
						if(dis+"_"+s_code not in d.keys()):
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
				
				
				elif(dis== common[3]):
					if(s_code == 'up'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'hp'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
				elif(dis == common[4]):
					if(s_code == "up"):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'rj'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
			for key, value in data.items():
				sub = key.split("/")
				if(sub[0]==dis):
					if(dis not in d.keys() and df1.loc[ind,'tag']=='delta'):
						d[dis] = {'id': data[key]['id'] , 'c':df1.loc[ind,'confirmed']}
					elif(dis in d.keys()):
						if(df1.loc[ind,'tag']=='delta'):
							d[dis] = {'id': data[key]['id'] , 'c' : d[dis]['c']+df1.loc[ind,'confirmed']}
						elif(df1.loc[ind,'tag'] == 'total' and d[dis]['c']<df1.loc[ind,'confirmed']):
							d[dis] = {'id': data[key]['id'] , 'c':df1.loc[ind,'confirmed']-d[dis]['c'] }
					break
		
		for k, v in d.items():
			writer.writerow([v['id'],w,v['c']])

		start = date
		w+=1
	f.close()

df = pd.read_csv('cases-week.csv',header=None)
df.columns = ['districtid', 'weekid', 'cases']
df = df.sort_values(by=['districtid'])
df.to_csv('cases-week.csv' , index=False)


#monthly cases district wise
df = pd.read_csv('data.csv')

def get_next_month(date):
    month = (date.month%12)+1
    year = date.year + (date.month + 1 > 12)
    return dt.datetime(year, month, 1)

start = dt.datetime(2020,3,15)
end = dt.datetime(2020,9,5)
date = dt.datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S')
m=1
with open('cases-month.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	while(date.date()<=end.date()):
		date = get_next_month(start)
		days = start
		d = {}
		df1 = pd.DataFrame()

		while(days<date and days<=end):
			i = df['date'] == str(days.date())
			df1 = df1.append(df[i])
			days=days+timedelta(days=1)
		
		for ind in df1.index:
			dis = df1.loc[ind,'district'].lower()
			s_code = df1.loc[ind,'state'].lower()

			if(s_code in state_code and dis in others):
				
				if((dis+"_"+s_code) not in d.keys()):
					d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c': df1.loc[ind,'confirmed']}
				else:
					if(df1.loc[ind,'tag']=='delta'):
						d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c':d[dis+'_'+s_code]['c']+df1.loc[ind,'confirmed']}
					elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
						d[dis+'_'+s_code] = {'id': data['unknown_'+s_code]['id'], 'c':df1.loc[ind,'confirmed']-d[dis+'_'+s_code]['c']}
				

			if(dis in common):
				
				if(dis == common[0]):
					if(s_code == "br"):
						if((dis+"_"+s_code) not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["aurangabad/Q43086"]['id'], 'c':df1.loc[ind,'confirmed']-d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'mh'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c': df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id':data["aurangabad/Q592942"]['id'], 'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
				elif(dis == common[1]):
					if(s_code == 'ct'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c': df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q16056268"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'up'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["balrampur/Q1948380"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
				
				
				elif(dis == common[2]):
					if(s_code == 'ct'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q100157"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

					elif(s_code == 'hp'):
						if(dis+"_"+s_code not in d.keys()):
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["bilaspur/Q1478939"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
				
				
				elif(dis== common[3]):
					if(s_code == 'up'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2019757"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'hp'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["hamirpur/Q2086180"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
				elif(dis == common[4]):
					if(s_code == "up"):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = { 'id': data["pratapgarh/Q1473962"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}
					
					elif(s_code == 'rj'):
						if(dis+"_"+s_code not in d.keys()):
							d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c':df1.loc[ind,'confirmed']}
						else:
							if(df1.loc[ind,'tag']=='delta'):
								d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c': d[dis+"_"+s_code]['c']+df1.loc[ind,'confirmed']}
							elif(df1.loc[ind,'tag'] == 'total' and d[dis+'_'+s_code]['c']<df1.loc[ind,'confirmed']):
								d[dis+"_"+s_code] = {'id': data["pratapgarh/Q1585433"]['id'],'c':df1.loc[ind,'confirmed']- d[dis+"_"+s_code]['c']}

				
			for key, value in data.items():
				sub = key.split("/")
				if(sub[0]==dis):
					if(dis not in d.keys() and df1.loc[ind,'tag']=='delta'):
						d[dis] = {'id': data[key]['id'] , 'c':df1.loc[ind,'confirmed']}
					elif(dis in d.keys()):
						if(df1.loc[ind,'tag']=='delta'):
							d[dis] = {'id': data[key]['id'] , 'c':d[dis]['c']+df1.loc[ind,'confirmed']}
						elif(df1.loc[ind,'tag'] == 'total' and d[dis]['c']<df1.loc[ind,'confirmed']):
							d[dis] = {'id': data[key]['id'] , 'c':df1.loc[ind,'confirmed']-d[dis]['c'] }
					break

		for k, v in d.items():
			writer.writerow([v['id'],m,v['c']])

		start = date
		m+=1
	f.close()

df = pd.read_csv('cases-month.csv',header=None)
df.columns = ['districtid', 'monthid', 'cases']
df = df.sort_values(by=['districtid'])
df.to_csv('cases-month.csv' , index=False)


#overall cases district wise
df = pd.read_csv("cases-month.csv")

with open('cases-overall.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	d={}
	for ind, row in df.iterrows():
		t=0
		df1 = df.loc[df['districtid']==row['districtid']]
		
		for i,r in df1.iterrows():
			t+=r['cases']

		d[row['districtid']] = {'id': row['districtid'], 'c':t}
	
	for key, value in d.items():
		writer.writerow([value['id'],'1',value['c']])

	f.close()

df = pd.read_csv('cases-overall.csv',header=None)
df.columns = ['districtid', 'timeid', 'cases']
df = df.sort_values(by=['districtid'])
df.to_csv('cases-overall.csv' , index=False)

