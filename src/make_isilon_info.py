import datetime
import random
from src.aux_info_maker import makeAuxInfo
import uuid

def makeIsilonInfo(volume):
    aa = {
        "id":uuid.uuid1(),
        "cluster_id":"cluster01",
        "percentage":65,
        "volume":volume
    }
    return aa
