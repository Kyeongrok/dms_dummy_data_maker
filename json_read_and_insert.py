import json, uuid
from elasticsearch import Elasticsearch

es = Elasticsearch() # 기본값 localhost

try:
    es.indices.create(index="instance")
except Exception as e:
    print(e)

def getJsonObj(fileName):
    file = open(fileName)
    return json.loads(file.read())

def insertToEs(indexName, doc):
    # id를 생성해서 es에 넣는다.
    doc['id'] = uuid.uuid1()
    res = es.create(index=indexName, doc_type="_doc", id=doc['id'], body=doc)
    print(res)


jsonObj = getJsonObj("instance.json")
print(jsonObj)

for instance in jsonObj:
    insertToEs("instance", instance)

