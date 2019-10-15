import http.client, json, ssl, base64

def convertByteToGiga(byte):
	return byte / 1024 / 1024 / 1024

def getApiResponse(query):
	auth = str.encode("%s:%s" % ('root', ''))
	user_and_pass = base64.b64encode(auth).decode("ascii")
	headers = {"Authorization":"Basic {}".format(user_and_pass),
			   "Accept":"application/json"}
	conn = http.client.HTTPSConnection('10.230.101.102', 8080, context=ssl._create_unverified_context())
	conn.request("GET", query, headers=headers)
	res = conn.getresponse()
	return res

#res = getApiResponse("/platform/1/statistics/current?key=node.sysfs.root.bytes.used")
#res = getApiResponse("/platform/1/statistics/current?key=node.sysfs.var.percent.free")
res = getApiResponse("/platform/5/statistics/current?key=cluster.alert.info")
data = res.read()
result = json.loads(data.decode('utf-8'))
#print(res.status, res.reason)
#print(res.getheaders())
print(result)
#value = result['stats'][0]['value']
#print(convertByteToGiga(value))

