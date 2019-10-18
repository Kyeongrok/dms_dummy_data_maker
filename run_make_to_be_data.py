from src.make_to_be_data import makeAsIsData
from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=["10.230.102.12"])
#es.indices.create(index="as_is_data")

for i in range(3000):
    doc = makeAsIsData()
    print(doc)
    res = es.create(index="as_is_data", id=doc['id'], body=doc)

