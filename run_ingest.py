import os, sys, random
from elasticsearch import Elasticsearch
from os.path import expanduser
from time import sleep
from maker.fileMaker import make as makeFile
from maker.fileMaker import make as copyFile
from datetime import datetime
from src.run_file_io import sendIoLogToElasticSearch
import uuid
from src.make_file_io import makeFileIo

home = expanduser("~")
print("home dir:", home)
# elastic search가 올라가 있는 서버의 ip또는 domain으로 바꾼다.
#es = Elasticsearch(hosts=["c2-13-125-237-227.ap-northeast-2.compute.amazonaws.com"])

# 기본값은 localhost이다.
es = Elasticsearch()
# es.indices.create(index="ingest_log")

def makeMetaInfo():
    formattedDate = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    rndItem = lambda list: list[random.randint(0, len(list) - 1)]
    info = {
        "id": uuid.uuid1(),
        "station":"poc1.station.com",
        "employee_id":rndItem(["1620282", "1520332"]),
        "vin":rndItem(["N1234567", "N1234568"]),
        "datetime":formattedDate,
        "status":"inactive",
        "maker":rndItem(["HMC", "Mobis", "Partners"]),
        "department":rndItem(["1259", "1438"]),
        "target_system":rndItem(["HDP", "Robotaxi"]),
        "sensors":rndItem(["FR_C_LDR", "RR_C_LDR", "RF_LDR", "RF_MD_LDR", "RF_SD_LDR",
                           "INT_LDR"]
                          ),
        "ladir_count":rndItem([1,2,3,4,5]),
        "location":rndItem(["seoul","uiwang","pangyo","sejong","etc"])
    }
    return info

def makeDirName(metaInfo):
    dirName = "/{}/{}/{}/{}/{}/{}/{}/{}/"\
        .format(metaInfo["vin"],
                metaInfo["maker"],
                metaInfo["department"],
                metaInfo["target_system"],
                metaInfo["sensors"],
                metaInfo["datetime"],
                metaInfo["ladir_count"],
                metaInfo["location"]
                )
    return dirName

metaInfo = makeMetaInfo()
dirName = makeDirName(metaInfo)
fromPath = "{}/usb{}".format(home, dirName)
toPath = "{}/mnt{}".format(home, dirName)

def run():
    print("from:",fromPath)
    print("to:",toPath)

    res = makeFile(fromPath, "data.bin")
    print("start copy")

    now = datetime.now()
    formattedDate = now.strftime("%Y-%m-%d %H:%M:%S")
    doc = makeFileIo(metaInfo['id'],
                     metaInfo['station'],
                     metaInfo['employee_id'],
                     fromPath,
                     toPath,
                     metaInfo["status"],
                     formattedDate)
    # sleep(5)
    res = es.create(index="io_log", doc_type="_doc", id=doc['id'], body=doc)
    id = metaInfo['id']
    sleep(20)
    #
    # print("copying file from usb to isilon")
    # sleep(1)
    # copyFile(toPath,"data.bin")
    print("ingest success")
    doc["status"] = "active"
    res = es.update(index="io_log", doc_type="_doc", id=id, body={"doc":doc})

    doc = {
        "id":uuid.uuid1(),
        "cluster_id":"cluster01",
        "percentage":65,
        "volume":1
    }
    res = es.create(index="isilon_info", id=doc['id'], body=doc)
    print(res)

run()
