# Check if ip is different from the ip stored in the file
# in case there is a new ip the file is updated and a message is send via pushbullet with the help of push.py
import ipgetter
from subprocess import call

myFile=open('ip.txt','r+')
saved_ip=myFile.read()
ip = ipgetter.myip()
print (ip)
if ip<>saved_ip:
	myFile.seek(0)
	myFile.truncate()
	myFile.write(ip)
	call(["python","push.py",ip])
else:
	print ("old ip is "+saved_ip)
myFile.close()

