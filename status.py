# python script that displays the internal and external ip on the screen
# Conditions: Linux, figlet

import socket
import os
import time
import ipgetter

def bprint(text):
	os.system("figlet -f big "+text)

semaforo=True
os.environ['LINES'] = "25"
os.environ['COLUMNS'] = "80"
ip=([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
ip=ip.replace("."," . ")
extip=ipgetter.myip()
extip=extip.replace("."," . ")

while semaforo:
	os.system(r'clear')
	print ("ip interno:")
	bprint (ip)
	print ("ip externo")
	bprint (extip)
	time.sleep(2)
