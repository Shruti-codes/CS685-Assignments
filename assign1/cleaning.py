import json

with open('neighbor-districts.json') as f:
	data = json.load(f)
	f.close()

assam_districts = {'c': 'as', 'd' : ['baksa','barpeta','bishwanath','bongaigaon','cachar','charaideo','chirang','darrang','dhemaji',
'dhubri','dibrugarh', 'dima hasao', 'goalpara', 'golaghat', 'hailakandi', 'hojai', 'jorhat','kamrup metropolitan',
'kamrup', 'east karbi anglong', 'karimganj','kokrajhar','lakhimpur','majuli','morigaon','nagaon','nalbari','sivasagar',
'sonitpur','south salmara mankachar','tinsukia','udalguri','west karbi anglong'] }

manipur_districts ={ 'c':'mn', 'd' : ['bishnupur','chandel','churachandpur','imphal east','imphal west','jiribam','kakching','kamjong',
'kangpokpi','noney','pherzawl','senapati','tamenglong','tengnoupal','thoubal','ukhrul'] }

sikkim_districts = {'c':'sk' , 'd': ['east sikkim', 'north sikkim','south sikkim','west sikkim'] }

telangana_districts = {'c':'tg', 'd': ['bhadradri kothagudem','hyderabad','jagtial','jangaon','jayashankar bhupalapally',
'jogulamba gadwal', 'kamareddy','karimnagar','khammam','komram bheem','mahabubabad','mahabubnagar','mancherial',
'medak','medchal malkajgiri','mulugu','nagarkurnool','nalgonda','narayanpet','nirmal','nizamabad','peddapalli',
'rajanna sircilla','ranga reddy','sangareddy','siddipet','suryapet','vikarabad','wanaparthy','warangal rural',
'warangal urban','yadadri bhuvanagiri'] }

goa_districts = {'c':'ga', 'd': ['north goa', 'south goa'] }

#data cleaning

qd = "Q987"	#for delhi
data = {key.replace("_district",''):value for key,value in data.items()}	#remove suffix '_district'

for key,value in list(data.items()):
	for x in range(len(value)):

		if("_district" in value[x]):
			sub = value[x].split("_district")
			value[x] = sub[0]+sub[1]
		if(value[x].startswith("ri-bhoi")):
			value[x] = value[x].replace("-",'')

		if("-" in value[x]):
			sub = value[x].split("-")
			value[x] = sub[0]+" "+sub[1]

		elif("delhi" in value[x] or 'shahdara' in value[x]):
			value[x] = "delhi/"+qd
		elif(value[x] == "bijapur/Q1727570"):
			value[x] = "vijayapura/Q1727570"
		elif(value[x] == "bijapur/Q100164"):
			continue
		elif("pashchimi" in value[x]):
			value[x] = value[x].replace("pashchimi", "west")
		elif("pashchim" in value[x]):
			value[x] = value[x].replace("pashchim", "west")
		elif("purba" in value[x] and "medinipur" not in value[x] and 'bardhaman' not in value[x]):
			value[x] = value[x].replace("purba", "east")
		elif("purbi" in value[x] ):
			value[x] = value[x].replace("purbi", "east")
		elif(value[x].startswith('nav_sari')):
			value[x] = value[x].replace('_', '')
			continue
		elif(value[x].startswith('rae_bareilly')):
			sub = value[x].split("/")
			value[x] = 'rae bareli/'+sub[1]
		elif(value[x].startswith('panch_mahal')):
			value[x] = value[x].replace('_', '')
			continue
		elif(value[x].startswith('sabar')):
			value[x] = value[x].replace('_', '')
			continue
		elif(value[x].startswith('sait')):
			sub = value[x].split("/")
			value[x] = "sant kabir nagar/"+sub[1]
			continue
		elif(value[x].startswith('seraikela_kharsawan')):
			sub = value[x].split("/")
			value[x] = "saraikela-kharsawan/"+sub[1]
			continue
		elif(value[x].startswith('shaheed_bhagat')):
			sub = value[x].split("/")
			value[x] = "shahid bhagat singh nagar/"+sub[1]
			continue
		elif(value[x].startswith('siddharth')):
			sub = value[x].split("/")
			value[x] = "siddharthnagar/"+sub[1]
			continue
		elif(value[x].startswith('sri_potti_sriramulu_nellore')):
			sub = value[x].split("/")
			value[x] = 's.p.s. nellore/'+sub[1]
			continue
		elif(value[x].startswith('the_dangs')):
			sub = value[x].split("/")
			value[x] = 'dang/'+sub[1]
			continue
		elif(value[x].startswith('ambedkar')):
			sub = value[x].split("/")
			value[x] = 'ambedkar nagar/'+sub[1]
		elif(value[x].startswith('ashok')):
			sub = value[x].split("/")
			value[x] = 'ashoknagar/'+sub[1]
		elif(value[x].startswith('banas')):
			sub = value[x].split("/")
			value[x] = 'banaskantha/'+sub[1]
		elif(value[x].startswith('bangalore_rural')):
			sub = value[x].split("/")
			value[x] = 'bengaluru rural/'+sub[1]
		elif(value[x].startswith('bangalore_urban')):
			sub = value[x].split("/")
			value[x] = 'bengaluru urban/'+sub[1]
		elif(value[x].startswith('devbhumi_dwaraka')):
			sub = value[x].split("/")
			value[x] = 'devbhumi dwarka/'+sub[1]
		elif(value[x].startswith('fategarh_sahib')):
			sub = value[x].split("/")
			value[x] = 'fatehgarh sahib/'+sub[1]
		elif(value[x].startswith('jyotiba')):
			sub = value[x].split("/")
			value[x] = 'amroha/'+sub[1]
		elif(value[x].startswith('kaimur')):
			sub = value[x].split("/")
			value[x] = 'kaimur/'+sub[1]
		elif(value[x].startswith('sahibzada_ajit_singh_nagar')):
			sub = value[x].split("/")
			value[x] = 's.a.s. nagar/'+sub[1]
		

		if("_" in value[x]):
			sub = value[x].split("_",-1)
			if(len(sub)==2):
				value[x] = sub[0]+" "+sub[1]
			elif(len(sub)==3):
				value[x] = sub[0]+" "+sub[1]+" "+sub[2]
			elif(len(sub)==4):
				value[x] = sub[0]+" "+sub[1]+" "+sub[2]+" "+sub[3]
		
		if("the" in value[x]):
			value[x] = value[x].replace("the ","")

		sub = value[x].split("/")
		if(sub[0]=="anugul"):
			value[x] = "angul/"+sub[1]
		elif(sub[0]=='aizwal'):
			value[x] = "aizawl/"+sub[1]
		elif(value[x].startswith("ashok")):
			value[x] = value[x].replace("_",'')
		elif(sub[0]=='badgam'):
			value[x] = "budgam/"+sub[1]
		elif(value[x].startswith("baloda")):
			value[x]=value[x].replace("_",' ')
		elif(value[x].startswith("banas")):
			value[x]=value[x].replace("_",'')
		elif(sub[0]=='baramula'):
			value[x] = "baramulla/"+sub[1]
		elif(sub[0]=='baudh'):
			value[x] = "boudh/"+sub[1]
		elif(sub[0]=='bellary'):
			value[x] = "ballari/"+sub[1]
		elif(sub[0]=='chamarajanagar'):
			value[x] = 'chamarajanagara/'+sub[1]
		elif(sub[0]=='charkhi_dadri'):
			value[x] = 'charkhi dadri/'+sub[1]
		elif(sub[0]== 'dakshina_kannada'):
			value[x] = 'dakshina kannada/'+sub[1]
		elif(sub[0]== 'dantewada'):
			value[x] = 'dakshin bastar dantewada/'+sub[1]
		elif(sub[0]== 'dhaulpur'):
			value[x] = 'dholpur/'+sub[1]
		elif(sub[0]=='firozpur'):
			value[x] = 'ferozepur/'+sub[1]
		elif(sub[0]=='gondiya'):
			value[x] = 'gondia/'+sub[1]
		elif(sub[0]=='jagatsinghapur'):
			value[x] = 'jagatsinghpur/'+sub[1]
		elif(sub[0]=='jajapur'):
			value[x] = 'jajpur/'+sub[1]
		elif(sub[0]=='jalor'):
			value[x] = 'jalore/'+sub[1]
		elif(sub[0]=='kanchipuram'):
			value[x] = 'kancheepuram/'+sub[1]
		elif(sub[0]=='kheri'):
			value[x] = 'lakhimpur kheri/'+sub[1]
		elif(sub[0]=='kochbihar'):
			value[x] = 'cooch behar/'+sub[1]
		elif(sub[0]=='kodarma'):
			value[x] = 'koderma/'+sub[1]
		elif(sub[0]=='lahul and spiti'):
			value[x] = 'lahaul and spiti/'+sub[1]
		elif(sub[0]=='mahesana'):
			value[x] = 'mehsana/'+sub[1]
		elif(sub[0]=='mahrajganj'):
			value[x] = 'maharajganj/'+sub[1]
		elif(sub[0]=='maldah'):
			value[x] = 'malda/'+sub[1]
		elif(sub[0]=='marigaon'):
			value[x] = 'morigaon/'+sub[1]
		elif(sub[0]=='muktsar'):
			value[x] = 'sri muktsar sahib/'+sub[1]
		elif(sub[0]=='mumbai city'):
			value[x] = 'mumbai/'+sub[1]
		elif(sub[0]=='nandubar'):
			value[x] = 'nandurbar/'+sub[1]
		elif(sub[0]=='narsimhapur'):
			value[x] = 'narsinghpur/'+sub[1]
		elif(sub[0]=='pakaur'):
			value[x] = 'pakur/'+sub[1]
		elif(sub[0]=='palghat'):
			value[x] = 'palakkad/'+sub[1]
		elif(sub[0]=='pattanamtitta'):
			value[x] = 'pathanamthitta/'+sub[1]
		elif(sub[0]=='puruliya'):
			value[x] = 'purulia/'+sub[1]
		elif(sub[0]=='rajauri'):
			value[x] = 'rajouri/'+sub[1]
		elif(sub[0]=='rangareddy'):
			value[x] = 'ranga reddy/'+sub[1]
		elif(value[x].startswith("sant ravidas")):
			value[x] = 'bhadohi/'+sub[1]
		elif(sub[0]=='sepahijala'):
			value[x] = 'sipahijala/'+sub[1]
		elif(sub[0]=='sharawasti'):
			value[x] = 'shrawasti/'+sub[1]
		elif(sub[0]=='shimoga'):
			value[x] = 'shivamogga/'+sub[1]
		elif(sub[0]=='shopian'):
			value[x] = 'shopiyan/'+sub[1]
		elif(sub[0]=='sivagangai'):
			value[x] = 'sivaganga/'+sub[1]
		elif(value[x].startswith('sri ganganagar')):
			value[x] = 'ganganagar/'+sub[1]
		elif(value[x].startswith('thoothukudi')):
			value[x] = 'thoothukkudi/'+sub[1]
		elif(value[x].startswith('tiruchchirappalli')):
			value[x] = 'tiruchirappalli/'+sub[1]
		elif(value[x].startswith('tirunelveli')):
			value[x] = 'tirunelveli/'+sub[1]
		elif(value[x].startswith('tiruvanamalai')):
			value[x] = 'tiruvannamalai/'+sub[1]
		elif(value[x].startswith('tumkur')):
			value[x] = 'tumakuru/'+sub[1]
		elif(value[x].startswith('yadagiri')):
			value[x] = 'yadgir/'+sub[1]
		elif(value[x].startswith('ysr')):
			value[x] = 'y.s.r. kadapa/'+sub[1]
		elif(value[x].startswith('baleshwar')):
			value[x] = 'balasore/'+sub[1]
		elif(value[x].startswith('belgaum')):
			value[x] = 'belagavi/'+sub[1]
		elif(value[x].startswith('debagarh')):
			value[x] = 'deogarh/'+sub[1]
		elif(value[x].startswith('faizabad')):
			value[x] = 'ayodhya/'+sub[1]
		elif(sub[0]=='bid'):
			value[x] = 'beed/'+sub[1]
		elif(value[x].startswith('hugli')):
			value[x] = 'hooghly/'+sub[1]
		elif(value[x].startswith('jhunjhunun')):
			value[x] = 'jhunjhunu/'+sub[1]
		elif(value[x].startswith('bemetara')):
			value[x] = 'bametara/'+sub[1]
		elif(value[x].startswith('kabirdham')):
			value[x] = 'kabeerdham/'+sub[1]
		elif(value[x].startswith('sonapur')):
			value[x] = 'subarnapur/'+sub[1]

		# elif(sub[0].startswith("east")):
		# 	sub1 = sub[0].split("_",-1)
		# 	if(len(sub1)==2):
		# 		value[x] = "east "+sub1[1]+"/"+sub[1]
		# 	elif(len(sub1)==3):
		# 		value[x] = "east "+sub1[1]+' '+sub1[2]+"/"+sub[1]

		elif(sub[0].endswith("east")):
			sub1 = sub[0].split("_",-1)
			if(len(sub1)==2):
				value[x] = sub1[0]+" east"+"/"+sub[1]

		elif(sub[0].endswith("west")):
			sub1 = sub[0].split("_",-1)
			if(len(sub1)==2):
				value[x] = sub1[0]+" west"+"/"+sub[1]

	sub=key.split("/")
	if(key.startswith("south_salmara-mankachar")):
		data["south salmara mankachar/"+sub[1]] = data.pop(key)
	elif('delhi' in key or key.startswith('shahdara')):
		data['delhi/'+qd] = data.pop(key)
	elif(key == "bijapur/Q1727570"):
		data["vijayapura/Q1727570"] = data.pop(key)
	elif(key == "bijapur/Q100164"):
		continue
	elif(key.startswith("lahul_and_spiti")):
		data["lahaul and spiti/"+sub[1]] = data.pop(key)
	elif(key.startswith("mumbai_city")):
		data["mumbai/"+sub[1]] = data.pop(key)
	elif(key.startswith("nav_sari")):
		data["navsari/"+sub[1]] = data.pop(key)
	elif(key.startswith("panch_mahal")):
		data["panchmahal/"+sub[1]] = data.pop(key)
	elif(key.startswith("rae_bareilly")):
		data["rae bareli/"+sub[1]] = data.pop(key)
	elif(key.startswith("ri-bhoi")):
		data['ribhoi/'+sub[1]] = data.pop(key)
	elif(key.startswith("sabar")):
		data["sabarkantha/"+sub[1]] = data.pop(key)
	elif(key.startswith("sait")):
		data["sant kabir nagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("sant_ravidas")):
		data["bhadohi/"+sub[1]] = data.pop(key)
	elif(key.startswith("sepahijala")):
		data["sipahijala/"+sub[1]] = data.pop(key)
	elif(key.startswith("seraikela_kharsawan")):
		data["saraikela-kharsawan/"+sub[1]] = data.pop(key)
	elif(key.startswith("shaheed_bhagat")):
		data["shahid bhagat singh nagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("siddharth")):
		data["siddharthnagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("sri_ganganagar")):
		data["ganganagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("sri_potti_sriramulu_nellore")):
		data["s.p.s. nellore/"+sub[1]] = data.pop(key)
	elif(key.startswith("the_dangs")):
		data["dang/"+sub[1]] = data.pop(key)
	elif(key.startswith("tirunelveli")):
		data["tirunelveli/"+sub[1]] = data.pop(key)
	elif(key.startswith("ambedkar")):
		data["ambedkar nagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("ashok")):
		data["ashoknagar/"+sub[1]] = data.pop(key)
	elif(key.startswith("banas")):
		data["banaskantha/"+sub[1]] = data.pop(key)
	elif(key.startswith("bangalore_rural")):
		data["bengaluru rural/"+sub[1]] = data.pop(key)
	elif(key.startswith("bangalore_urban")):
		data["bengaluru urban/"+sub[1]] = data.pop(key)
	elif(key.startswith("devbhumi_dwaraka")):
		data["devbhumi dwarka/"+sub[1]] = data.pop(key)
	elif(key.startswith("fategarh_sahib")):
		data["fatehgarh sahib/"+sub[1]] = data.pop(key)
	elif(key.startswith("jyotiba")):
		data["amroha/"+sub[1]] = data.pop(key)
	elif(key.startswith("kaimur")):
		data["kaimur/"+sub[1]] = data.pop(key)
	elif(key.startswith('sahibzada_ajit_singh_nagar')):
		data["s.a.s. nagar/"+sub[1]] = data.pop(key)

	elif("-" in key):
		sub=key.split('-')
		data[sub[0]+' '+sub[1]] = data.pop(key)
	elif("the_" in key):
		sub = key.split("the_")
		data[sub[1]]=data.pop(key)

	elif("pashchimi" in key):
		sub=key.split('pashchimi_')
		data["west "+sub[1]] = data.pop(key)
	elif("pashchim" in key):
		sub=key.split('pashchim_')
		data["west "+sub[1]] = data.pop(key)
	elif("purba" in key and "medinipur" not in key and 'bardhaman' not in key):
		sub=key.split('purba_')
		data["east "+sub[1]] = data.pop(key)
	elif("purbi" in key):
		sub=key.split('purbi_')
		data["east "+sub[1]] = data.pop(key)
	
	elif("_" in key):
		sub = key.split("_", -1)
		if(len(sub)==2):
			data[sub[0]+" "+sub[1]] = data.pop(key)
		elif(len(sub)==3):
			data[sub[0]+" "+sub[1]+" "+sub[2]] = data.pop(key)
		elif(len(sub)==4):
			data[sub[0]+" "+sub[1]+" "+sub[2]+" "+sub[3]] = data.pop(key)
	
	sub = key.split("/")
	if(key.startswith("anugul")):
		data["angul/"+sub[1]] = data.pop(key)
	elif(key.startswith('badgam')):
		data["budgam/"+sub[1]] = data.pop(key)
	elif(key.startswith("aizwal")):
		data["aizawl/"+sub[1]] = data.pop(key)
	elif(key.startswith("baramula")):
		data["baramulla/"+sub[1]] = data.pop(key)
	elif(key.startswith("baudh")):
		data["boudh/"+sub[1]] = data.pop(key)
	elif(key.startswith("bellary")):
		data["ballari/"+sub[1]] = data.pop(key)
	elif(key.startswith("chamarajanagar")):
		data["chamarajanagara/"+sub[1]] = data.pop(key)
	elif(key.startswith("dantewada")):
		data["dakshin bastar dantewada/"+sub[1]] = data.pop(key)
	elif(key.startswith("dhaulpur")):
		data["dholpur/"+sub[1]] = data.pop(key)
	elif(key.startswith("firozpur")):
		data["ferozepur/"+sub[1]] = data.pop(key)
	elif(key.startswith("gondiya")):
		data["gondia/"+sub[1]] = data.pop(key)
	elif(key.startswith("jagatsinghapur")):
		data["jagatsinghpur/"+sub[1]] = data.pop(key)
	elif(key.startswith("jajapur")):
		data["jajpur/"+sub[1]] = data.pop(key)
	elif(key.startswith("jalor")):
		data["jalore/"+sub[1]] = data.pop(key)
	elif(key.startswith("kanchipuram")):
		data["kancheepuram/"+sub[1]] = data.pop(key)
	elif(key.startswith("kheri")):
		data["lakhimpur kheri/"+sub[1]] = data.pop(key)
	elif(key.startswith("kochbihar")):
		data["cooch behar/"+sub[1]] = data.pop(key)
	elif(key.startswith("kodarma")):
		data["koderma/"+sub[1]] = data.pop(key)
	elif(key.startswith("mahrajganj")):
		data["maharajganj/"+sub[1]] = data.pop(key)
	elif(key.startswith("maldah")):
		data["malda/"+sub[1]] = data.pop(key)
	elif(key.startswith("marigaon")):
		data["morigaon/"+sub[1]] = data.pop(key)
	elif(key.startswith("muktsar")):
		data["sri muktsar sahib/"+sub[1]] = data.pop(key)
	elif(key.startswith("nandubar")):
		data["nandurbar/"+sub[1]] = data.pop(key)
	elif(key.startswith("narsimhapur")):
		data["narsinghpur/"+sub[1]] = data.pop(key)
	elif(key.startswith("pakaur")):
		data["pakur/"+sub[1]] = data.pop(key)
	elif(key.startswith("palghat")):
		data["palakkad/"+sub[1]] = data.pop(key)
	elif(key.startswith("pattanamtitta")):
		data["pathanamthitta/"+sub[1]] = data.pop(key)
	elif(key.startswith("puruliya")):
		data["purulia/"+sub[1]] = data.pop(key)
	elif(key.startswith("rajauri")):
		data["rajouri/"+sub[1]] = data.pop(key)
	elif(key.startswith("rangareddy")):
		data["ranga reddy/"+sub[1]] = data.pop(key)
	elif(key.startswith("sharawasti")):
		data["shrawasti/"+sub[1]] = data.pop(key)
	elif(key.startswith("shimoga")):
		data["shivamogga/"+sub[1]] = data.pop(key)
	elif(key.startswith("shopian")):
		data["shopiyan/"+sub[1]] = data.pop(key)
	elif(key.startswith("sivagangai")):
		data["sivaganga/"+sub[1]] = data.pop(key)
	elif(key.startswith("thoothukudi")):
		data["thoothukkudi/"+sub[1]] = data.pop(key)
	elif(key.startswith("tiruchchirappalli")):
		data["tiruchirappalli/"+sub[1]] = data.pop(key)
	elif(key.startswith("tiruvanamalai")):
		data["tiruvannamalai/"+sub[1]] = data.pop(key)
	elif(key.startswith("tumkur")):
		data["tumakuru/"+sub[1]] = data.pop(key)
	elif(key.startswith("yadagiri")):
		data["yadgir/"+sub[1]] = data.pop(key)
	elif(key.startswith("ysr")):
		data["y.s.r. kadapa/"+sub[1]] = data.pop(key)
	elif(key.startswith("baleshwar")):
		data["balasore/"+sub[1]] = data.pop(key)
	elif(key.startswith("belgaum")):
		data["belagavi/"+sub[1]] = data.pop(key)
	elif(key.startswith("debagarh")):
		data["deogarh/"+sub[1]] = data.pop(key)
	elif(key.startswith("faizabad")):
		data["ayodhya/"+sub[1]] = data.pop(key)
	elif(key=="bid/Q814037"):
		data["beed/"+sub[1]] = data.pop(key)
	elif(key.startswith("hugli")):
		data["hooghly/"+sub[1]] = data.pop(key)
	elif(key.startswith("jhunjhunun")):
		data["jhunjhunu/"+sub[1]] = data.pop(key)
	elif(key.startswith("mahesana")):
		data["mehsana/"+sub[1]] = data.pop(key)
	elif(key.startswith("bemetara")):
		data["bametara/"+sub[1]] = data.pop(key)
	elif(key.startswith("kabirdham")):
		data["kabeerdham/"+sub[1]] = data.pop(key)
	elif(key.startswith("sonapur")):
		data["subarnapur/"+sub[1]] = data.pop(key)

if('konkan division/Q6268840' in data.keys()):
		data.pop('konkan division/Q6268840',None)
if('noklak/Q48731903' in data.keys()):
	data.pop('noklak/Q48731903',None)
if("mumbai suburban/Q2085374" in data.keys()):
	data['mumbai/Q2341660'] = data.pop("mumbai suburban/Q2085374",None)
	data.pop("mumbai suburban/Q2085374",None)
if("adilabad/Q15211" in data.keys()):
	data.pop("adilabad/Q15211",None)
if("komram bheem/Q28170184" in data.keys()):
	data.pop("komram bheem/Q28170184",None)
if("nirmal/Q28169750" in data.keys()):
	data.pop("nirmal/Q28169750",None)
if("north goa/Q108234" in data.keys()):
	data.pop("north goa/Q108234",None)

data2 = data.copy()
for key,value in data2.items():
	
	sub = key.split("/")
	if(sub[0] in assam_districts['d']):
		data['unknown_'+assam_districts['c']] = data.pop(key,None)
	elif(sub[0] in manipur_districts['d']):
		data['unknown_'+manipur_districts['c']] = data.pop(key,None)
	elif(sub[0] in goa_districts['d']):
		data['unknown_'+goa_districts['c']] = data.pop(key,None)
	elif(sub[0] in sikkim_districts['d']):
		data['unknown_'+sikkim_districts['c']] = data.pop(key,None)
	elif(sub[0] in telangana_districts['d']):
		data['unknown_'+telangana_districts['c']] = data.pop(key,None)

	if('noklak/Q48731903' in value):
		value = list(filter(lambda x: x!= 'noklak/Q48731903' , value))
		data[key] = value
	if('konkan division/Q6268840' in value):
		value = list(filter(lambda x: x!= 'konkan division/Q6268840' , value))
		data[key] = value
	if('mumbai suburban/Q2085374' in value):
		value = list(filter(lambda x: x!= 'mumbai suburban/Q2085374' , value))
		data[key] = value
	if('adilabad/Q15211' in value):
		value = list(filter(lambda x: x!= 'adilabad/Q15211' , value))
		data[key] = value

	for x in value:
		sub1 = x.split("/")
		if(sub1[0] in assam_districts['d']):
			value = list(filter(lambda x1: x1!= x , value))
			if('unknown_'+assam_districts['c'] not in data.keys()):
				data['unknown_'+assam_districts['c']] = value
			else:
				data['unknown_'+assam_districts['c']]+=value
		
		elif(sub1[0] in manipur_districts['d']):
			value = list(filter(lambda x1: x1!= x , value))
			if('unknown_'+manipur_districts['c'] not in data.keys()):
				data['unknown_'+manipur_districts['c']] = value
			else:
				data['unknown_'+manipur_districts['c']]+=value

		elif(sub1[0] in goa_districts['d']):
			value = list(filter(lambda x1: x1!= x , value))
			if('unknown_'+goa_districts['c'] not in data.keys()):
				data['unknown_'+goa_districts['c']] = value
			else:
				data['unknown_'+goa_districts['c']]+=value

		elif(sub1[0] in sikkim_districts['d']):
			value = list(filter(lambda x1: x1!= x , value))
			if('unknown_'+sikkim_districts['c'] not in data.keys()):
				data['unknown_'+sikkim_districts['c']] = value
			else:
				data['unknown_'+sikkim_districts['c']]+=value

		elif(sub1[0] in telangana_districts['d']):
			value = list(filter(lambda x1: x1!= x , value))
			if('unknown_'+telangana_districts['c'] not in data.keys()):
				data['unknown_'+telangana_districts['c']] = value
			else:
				data['unknown_'+telangana_districts['c']]+=value

for key, value in data.items():
	for x in range(len(value)):
		sub = value[x].split("/")
		if(sub[0] in assam_districts['d']):
			value[x] = value[x].replace(value[x],'unknown_'+assam_districts['c'])
		elif(sub[0] in sikkim_districts['d']):
			value[x] = value[x].replace(value[x],'unknown_'+sikkim_districts['c'])
		elif(sub[0] in goa_districts['d']):
			value[x] = value[x].replace(value[x],'unknown_'+goa_districts['c'])
		elif(sub[0] in manipur_districts['d']):
			value[x] = value[x].replace(value[x],'unknown_'+manipur_districts['c'])
		elif(sub[0] in telangana_districts['d']):
			value[x] = value[x].replace(value[x],'unknown_'+telangana_districts['c'])
		

	if(key in value):
		value = list(filter(lambda x: x!= key, value))	#remove occurrence of key in value (eg. Delhi)
		data[key] = value

	if(len(value) == len(set(value))):
		data[key] = value
	else:
		data[key] = list(set(value))

for key, value in data.items():
	for x in range(len(value)):
		if(value[x]== "unknown_sk"):
			data['unknown_sk'].append(key)
		if(value[x] == "unknown_mn"):
			data['unknown_mn'].append(key)
		if(value[x] == "unknown_tg"):
			data['unknown_tg'].append(key)

with open("neighbor-districts-modified.json", "w") as outfile:
	json.dump(data, outfile, indent = 2, sort_keys=True)
	outfile.close()

f=open("neighbor-districts-modified.json")
data = json.load(f)
f.close()

i=101
for key, value in data.items():
	data[key] = {'id':i, 'neighbors': value}
	i+=1

with open("neighbor-districts-modified.json", "w") as outfile:
	json.dump(data, outfile, indent = 2, sort_keys=True)
	outfile.close()

# airport quarantine
# bsf camp
# capf personnel
# chengalpattu
# evacuees
# foreign evacuees
# gaurela pendra marwahi
# hnahthial
# italians
# khawzawl
# lakshadweep
# mirpur
# muzaffarabad
# nicobars
# north and middle andaman
# other region
# other state
# others
# railway quarantine
# ranipet
# saitual
# south andaman
# tenkasi
# tirupathur
# unassigned
# unknown
# yanam

#Common Names
# hamirpur  -> UP, HP
# pratapgarh -> UP, RJ
#  balrampur ->UP, CT
#  aurangabad -> MH, BR
#  bilaspur -> CT, HP