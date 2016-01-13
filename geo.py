#!python3
# -*- coding: utf-8 -*

import csv
import requests

def geoProcess(geoDate, geoLink):
	print (geoDate)
	print (geoLink)
	


urlMontijo ='http://geopt.dyndns.org/Geopt_Statistics/RSS_latestpublished_PT.aspx?distrito=Setúbal&concelho=Montijo&tipoCache=Todos'
r = requests.get(urlMontijo.strip())
url_text = (r.text).split()
for p in range(0,len(url_text)):
	if "<link>" in url_text[p]:
		geoDate=(url_text[p-1])[:-17]
		geoLink = ((url_text[p])[:-7])[6:]
		geoProcess(geoDate, geoLink)

