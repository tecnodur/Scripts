#! /usr/bin/env python
# Simple script to send pushbullet messages. Must use a valid token
import json
import urllib2
import sys
 
#this is not a valid token, get your access token from https://www.pushbullet.com/#settings
token = "notvalidtoken"
recepient = "recepient@email.com"
 
if (len(sys.argv) < 2):
    print "USAGE: %s <message>" % (sys.argv[0])
    sys.exit()
 
a = sys.argv
a.pop(0)
message = " ".join(a)
 
jdata = json.dumps({"email": recepient,
                    "type": "note",
                    "title": "pypush",
                    "body": message})
 
request = urllib2.Request("https://api.pushbullet.com/v2/pushes",
                          headers={"Authorization": "Bearer %s" % (token),
                                   "Content-Type": "application/json"})
 
contents = urllib2.urlopen(request, jdata).read()
 
print contents
