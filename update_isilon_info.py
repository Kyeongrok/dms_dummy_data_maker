import random
import uuid
from src.make_isilon_info import makeIsilonInfo

import time
from datetime import datetime
from elasticsearch import Elasticsearch
import json
from call_isilon_api import ApiCaller

# es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
es = Elasticsearch()
apiCaller = ApiCaller("10.35.106.35", "root", "a")

def getIsilonVolume():
    # isilon에서 데이터를 가져옴

    return 10

volume = getIsilonVolume()

doc = makeIsilonInfo(volume)
doc = apiCaller.getAvailFreeTotal()

#es.indices.create(index="space_info")
res = es.create(index="space_info", id=doc['id'], body=doc)
print(res)
# INGEST하면 용량올라가는 기능
# 전체 용량 dash board
# to be dashboard 더미데이터 생성
# 초당 70mb

