import random
import uuid
from src.make_isilon_info import makeIsilonInfo

import time
from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
# es = Elasticsearch()

# es.indices.create(index="isilon_info")

def getIsilonVolume():
    # isilon에서 데이터를 가져옴

    return 10

volume = getIsilonVolume()

doc = makeIsilonInfo(volume)
doc = {
        "id":uuid.uuid1(),
        "cluster_id":"cluster01",
        "percentage":65,
        "volume":volume
    }
res = es.create(index="isilon_info", id=doc['id'], body=doc)

# INGEST하면 용량올라가는 기능
# 전체 용량 dash board
# to be dashboard 더미데이터 생성
# 초당 70mb

