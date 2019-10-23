import http.client, json, ssl, base64

def getPassword():
	# rsa방식 등의 암호화 된 코드를
	# 인증서버에 공개키를 등록 해놓고 디코딩 해서 password를 만든다.
	return ""

def convertByteToTera(byte):
	return byte / 1000 / 1000 / 1000 / 1000

class ApiCaller():
	def __init__(self):
		pass

	def getApiResponse(self, query):
		# id와 pw를 바꾼다.
		auth = str.encode("%s:%s" % ('root', 'a'))
		user_and_pass = base64.b64encode(auth).decode("ascii")
		headers = {"Authorization":"Basic {}".format(user_and_pass),
				   "Accept":"application/json"}
		conn = http.client.HTTPSConnection('10.35.106.35', 8080, context=ssl._create_unverified_context())
		conn.request("GET", query, headers=headers)
		res = conn.getresponse()
		return res

apiCaller = ApiCaller()

#/platform/1/statistics/current?key=node.sysfs.root.bytes.used
#/platform/1/statistics/current?key=node.sysfs.var.percent.free
# res = getApiResponse("/platform/5/statistics/current?key=cluster.alert.info")
res = apiCaller.getApiResponse("/platform/5/statistics/current?key=ifs.bytes.avail")
data = res.read()
result = json.loads(data.decode('utf-8'))
#print(res.status, res.reason)
#print(res.getheaders())
print(result)
print(convertByteToTera(result['stats'][0]['value']))
