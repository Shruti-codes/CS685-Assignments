import csv
import pandas as pd

#weekly
header = ['weekid', 'method', 'spot', 'districtid1', 'districtid2', 'districtid3', 'districtid4', 'districtid5']

df1 = pd.read_csv('zscore-week.csv')
df2 = pd.read_csv('method-spot-week.csv')
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'weekid'], right_on = ['districtid', 'weekid'] )

w=1
with open('top-week.csv','w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(i for i in header)

	while(w<=26):
		df4 = df3[df3['weekid'] == w]
		
		#for cold and neighborhood
		df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='cold')]
		man = df5.nsmallest(5, ['neighborhoodzscore'])

		if(len(man)>0):
			l = man['districtid'].to_list()
			writer.writerow([w, 'neighborhood', 'cold', ','.join(str(num) for num in l)  ])

		#for hot and neighborhood
		df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='hot')]
		man = df5.nlargest(5, ['neighborhoodzscore'])

		if(len(man)>0):
			l = man['districtid'].to_list()
			writer.writerow([w, 'neighborhood', 'hot', ','.join(str(num) for num in l) ])
		
		
		#for cold and state
		df5 = df4[(df4['method']=='state') & (df4['spot']=='cold')]
		mas = df5.nsmallest(5, ['statezscore'])

		if(len(mas)>0):
			l = mas['districtid'].to_list()
			writer.writerow([w, 'state', 'cold', ','.join(str(num) for num in l)  ])

		#for hot and state
		df5 = df4[(df4['method']=='state') & (df4['spot']=='hot')]
		mas = df5.nlargest(5, ['statezscore'])
		
		if(len(mas)>0):
			l = mas['districtid'].to_list()
			writer.writerow([w, 'state', 'hot', ','.join(str(num) for num in l) ])

		w+=1

#monthly

header = ['monthid', 'method', 'spot', 'districtid1', 'districtid2', 'districtid3', 'districtid4', 'districtid5']

df1 = pd.read_csv('zscore-month.csv')
df2 = pd.read_csv('method-spot-month.csv')
df3 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'monthid'], right_on = ['districtid', 'monthid'] )

m=1
with open('top-month.csv','w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(i for i in header)

	while(m<=8):
		df4 = df3[df3['monthid'] == m]
		
		#for cold and neighborhood
		df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='cold')]
		man = df5.nsmallest(5, ['neighborhoodzscore'])

		if(len(man)>0):
			l = man['districtid'].to_list()
			writer.writerow([m, 'neighborhood', 'cold', ','.join(str(num) for num in l)  ])

		#for hot and neighborhood
		df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='hot')]
		man = df5.nlargest(5, ['neighborhoodzscore'])

		if(len(man)>0):
			l = man['districtid'].to_list()
			writer.writerow([m, 'neighborhood', 'hot', ','.join(str(num) for num in l) ])
		
		
		#for cold and state

		df5 = df4[(df4['method']=='state') & (df4['spot']=='cold')]
		mas = df5.nsmallest(5, ['statezscore'])

		if(len(mas)>0):
			l = mas['districtid'].to_list()
			writer.writerow([m, 'state', 'cold', ','.join(str(num) for num in l)])

		#for hot and state
		df5 = df4[(df4['method']=='state') & (df4['spot']=='hot')]
		mas = df5.nlargest(5, ['statezscore'])

		if(len(mas)>0):
			l = mas['districtid'].to_list()
			writer.writerow([m, 'state', 'hot', ','.join(str(num) for num in l) ])

		m+=1


#overall

header = ['timeid', 'method', 'spot', 'districtid1', 'districtid2', 'districtid3', 'districtid4', 'districtid5']

df1 = pd.read_csv('zscore-overall.csv')
df2 = pd.read_csv('method-spot-overall.csv')
df4 = pd.merge(df1, df2, how='left', left_on = ['districtid', 'timeid'], right_on = ['districtid', 'timeid'] )

with open('top-overall.csv','w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(i for i in header)
		
	#for cold and neighborhood
	df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='cold')]
	man = df5.nsmallest(5, ['neighborhoodzscore'])

	if(len(man)>0):
		l = man['districtid'].to_list()
		writer.writerow([1, 'neighborhood', 'cold', ','.join(str(num) for num in l)  ])

	
	#for hot and neighborhood
	df5 = df4[(df4['method']=='neighborhood') & (df4['spot']=='hot')]
	man = df5.nlargest(5, ['neighborhoodzscore'])
	
	if(len(man)>0):
		l = man['districtid'].to_list()
		writer.writerow([1, 'neighborhood', 'hot', ','.join(str(num) for num in l) ])
			
	
	#for cold and state

	df5 = df4[(df4['method']=='state') & (df4['spot']=='cold')]
	mas = df5.nsmallest(5, ['statezscore'])

	if(len(mas)>0):
		l = mas['districtid'].to_list()
		writer.writerow([1, 'state', 'cold', ','.join(str(num) for num in l)])
	
	
	#for hot and state
	df5 = df4[(df4['method']=='state') & (df4['spot']=='hot')]
	mas = df5.nlargest(5, ['statezscore'])
	
	if(len(mas)>0):
		l = mas['districtid'].to_list()
		writer.writerow([1, 'state', 'hot', ','.join(str(num) for num in l) ])
