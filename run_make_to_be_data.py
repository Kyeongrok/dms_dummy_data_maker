from src.make_to_be_data import makeAsIsData
from elasticsearch import Elasticsearch


#es = Elasticsearch(hosts=["10.230.102.12"])
#es.indices.create(index="as_is_data")

docs = []

for i in range(10):
    doc = makeAsIsData()
    doc["id"] = "empty"
    docs.append(doc)
    print(doc)
    # res = es.create(index="as_is_data", id=doc['id'], body=doc)

import json

file = open("./dd.json", "w+")
file.write(json.dumps(docs))
