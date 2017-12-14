import sys
import requests
import json

hash ="%s" % sys.argv[1]


#API-Parameter
url = "http://localhost:14265"
header = {'Content-Type': 'application/json', 'X-IOTA-API-Version': '1'}


#get Tryte
req = requests.post(url, headers = header, data = json.dumps({'command': 'getTrytes', 'hashes': [hash]}))
tryte = req.text.split('"')[3]


#get new branch and trunk from tips
req2 = requests.post(url, headers = header, data = json.dumps({'command': 'getTips'}))
branch = req2.text.split('","')[278]
trunk = req2.text.split('","')[1337]


#attach to tangle
print('POW takes some time plz  wait....')
req3 = requests.post(url, headers = header, data = json.dumps({'command': 'attachToTangle', 'trunkTransaction': trunk, 'branchTransaction': branch, 'minWeightMagnitude': 18, 'trytes': [tryte]}))
print(req3.text)
newtryte = req3.text.split('"')[3]


#broadcast new tryte
req4 = requests.post(url, headers = header, data = json.dumps({'command': 'broadcastTransactions', 'trytes':[newtryte]}))
print(req4.text)


