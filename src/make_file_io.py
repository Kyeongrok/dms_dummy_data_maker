import datetime
import random
from src.aux_info_maker import makeAuxInfo

def makeFileIo(id, station, user, fromDir, toDir, status, datetime):
    aa = {
        "id":id,
        "station":station,
        "user":user,
        "fromDir":fromDir,
        "toDir":toDir,
        "status":status,
        "datetime":datetime
    }
    return aa
