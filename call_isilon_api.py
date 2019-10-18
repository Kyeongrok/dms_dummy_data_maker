import http.client, json, ssl, base64

def getPassword():
	# rsa방식 등의 암호화 된 코드를
	# 인증서버에 공개키를 등록 해놓고 디코딩 해서 password를 만든다.
	return ""

def getApiResponse(query):
	# id와 pw를 바꾼다.
	auth = str.encode("%s:%s" % ('root', ''))
	user_and_pass = base64.b64encode(auth).decode("ascii")
	headers = {"Authorization":"Basic {}".format(user_and_pass),
			   "Accept":"application/json"}
	conn = http.client.HTTPSConnection('10.230.101.102', 8080, context=ssl._create_unverified_context())
	conn.request("GET", query, headers=headers)
	res = conn.getresponse()
	return res

#/platform/1/statistics/current?key=node.sysfs.root.bytes.used
#/platform/1/statistics/current?key=node.sysfs.var.percent.free
res = getApiResponse("/platform/5/statistics/current?key=cluster.alert.info")
data = res.read()
result = json.loads(data.decode('utf-8'))
#print(res.status, res.reason)
#print(res.getheaders())
print(result)

