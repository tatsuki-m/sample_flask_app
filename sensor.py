from datetime import datetime
from collections import OrderedDict
import subprocess as sb
import sys
import json
import time, random
import requests
import pprint

SEND_NUM = 100
SLP_TIME = 3
IP = "http://192.168.10.1"
PORT = 8080
endpoint='sensor'
params = {}
seq_num = 0

def netcat(ipaddr, port):
       cmd = 'nc %s %s' % (ipaddr, port)
       return sb.Popen(cmd.split(),stdin=sb.PIPE)#encoding='utf8')

def send_request(ip_addr, port, params):
    response = requests.get(
            '{0}:{1}/{2}'.format(ip_addr, port, endpoint),
            params=params)
    print(response)
    #pprint.pprint(response.json())

#ncPipe = netcat(IP, PORT)

for i in range(SEND_NUM):
    date = datetime.now().replace(microsecond=0).isoformat()
    temperature = random.randint(0,100)
    params["device_id"] = 1
    params["date"] = date
    params["temperature"] = temperature
    params["seq_num"] = seq_num
    print(params)
    #msg = json.dumps(dict)
    #msg += "\n"
    #print(msg)
    #ncPipe.stdin.write(str(msg))
    #ncPipe.stdin.flush()
    #with open('normal.json', 'wt') as f:
    #    json.dump(dict, f)
    #print(dict)

    msg = json.dumps(params)
    send_request(IP, PORT, params)
    seq_num+=1
    time.sleep(SLP_TIME)
