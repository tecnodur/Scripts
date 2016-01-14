#!python3
# -*- coding: utf-8 -*

import csv
import requests
from subprocess import call

def geoProcess(geoDate, geoLink, concelho):
	if not geoLink.startswith('http'): return
	found = False
	cod = geoLink[18:]
	reader = csv.reader(open('list.csv',"r"), delimiter=";")
	for row in reader:
			if row[1]==cod:
				found = True
	if found is False:
		writer = csv.writer(open('list.csv','a'), delimiter=";")
		writer.writerow([concelho, cod,geoDate, geoLink])
		call(["python","push.py",('New geocahing found by durbot '+geoLink)])



localidadesFile = open ("localidades.csv")
localidadesContent= localidadesFile.readlines()
#print (localidadesContent)
for local in localidadesContent:
	local = local.split()
	distrito = local[0]
	concelho = local [1]
	url ='http://geopt.dyndns.org/Geopt_Statistics/RSS_latestpublished_PT.aspx?distrito='+distrito+'&concelho='+concelho+'&tipoCache=Todos'
#	print (url)
	r = requests.get(url.strip())
	url_text = (r.text).split()
	for p in range(0,len(url_text)):
		if "<link>" in url_text[p]:
#			print(url_text[p])
			geoDate=(url_text[p-1])[:-17]
			geoLink = ((url_text[p])[:-7])[6:]
			geoProcess(geoDate, geoLink, concelho)
