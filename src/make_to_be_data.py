import datetime
import random
import uuid

def makeAsIsData():
    logItems = [
        {"key": "test_car_no", "value": ["N333444", "N555666", "N223456", "N123457"]},
        {"key": "data_maker", "value": ["HMC","Mobis","Partners"]},
        {"key": "team_code", "value": ["1259", "1438", "2347", "1249"]},
        {"key": "target_system", "value": ["HDR", "Robotaxi", "SVM", "boopum1"]},
        {"key": "sensors", "value": ["FR_C_LDR", "RR_C_LDR", "RF_LDR", "RF_MD_LDR", "RF_SD_LDR", "INT_LDR"]},
        {"key": "ladir_count", "value": [1,2,3,4,5]},
        {"key": "location", "value": ["seoul","uiwang","pangyo","sejong","etc"]}
    ]
    rndItem = lambda list: list[random.randint(0, len(list)-1)]
    obj = {}

    for logItem in logItems:
        obj[logItem['key']] = rndItem(logItem['value'])
        formattedDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        obj["datetime"] = formattedDate
        obj["id"] = uuid.uuid1()
        obj["data_volume"] = random.randint(1, 2)

    return obj


