#!/usr/bin/python
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime
import json
import urllib2


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("smartplant/#")


def on_message(client, userdata, msg):
	try:
		data = "{\"user_id\": \"" + str(getserial()) + "\", \"datetime\":\"" + str(datetime.now()) + "\", " + str(msg.payload);
		req = urllib2.Request('https://sleepy-depths-29132.herokuapp.com/api/sensors')
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, data)
		print(data)
	except:
		print "Data or ethernet error"
  


def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial
 
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.24.1.1", 1883, 60)

client.loop_forever()