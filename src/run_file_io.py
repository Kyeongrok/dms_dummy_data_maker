import random

import time
from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
# es = Elasticsearch()

# es.indices.create(index="io_log")

def sendIoLogToElasticSearch(index, doc):
    res = es.create(index=index, id=doc['id'], body=doc)
    print(res)


