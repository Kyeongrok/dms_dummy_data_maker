import os
def make(path, fileName):
    # dir에 지정한 이름의 파일을 만든다
    try:
        filePath = "{}/{}".format(path, fileName)
        print(filePath)
        os.makedirs(path, 755)
        file = open(filePath, "w+")
        file.write("000000000000")
        return 1
    except Exception as e:
        return 0

