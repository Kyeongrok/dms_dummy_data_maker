from datetime import datetime
from elasticsearch import Elasticsearch
from src.make_as_is_data import makeLogObject
from src.aux_info_maker import makeAuxInfo

es = Elasticsearch() # 기본값 localhost
# elastic search 서버를 바꾸고 싶으면 아래 hosts값을 해당 server ip또는 domain으로 바꿔준다.
#es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])

es.indices.create(index="log_object")

# 개수를 조절 할 수 있다. 지금은 1000개를 넣는다.
for i in range(1000):
    now = datetime.now()
    logObj = makeLogObject(now)
    aux_info = makeAuxInfo()
    logObj.update(aux_info)
    res = es.create(index="log_object", id=aux_info['id'], body=logObj)
    print(i, res)
# 대전으로 가는 길에 뭐가 가장 많은가?


