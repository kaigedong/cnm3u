from collections import OrderedDict

whiteList = OrderedDict()
blackList = {}

# 读取白名单
with open("whitelist.txt", 'r') as fin:
    for aline in fin:
        aline = aline.strip()
        if aline != "":
            whiteList[aline] = []
# 读取黑名单
with open("blacklist.txt", "r") as fin:
    for aline in fin:
        aline = aline.strip()
        if aline != "":
            blackList[aline] = 1


def isInWhite(aStr, nextStr):
    for aItem in whiteList:
        if aItem in aStr:
            whiteList[aItem].append([aStr, nextStr])
            return True
    return False


def printWhite():
    for aWhite in whiteList:
        for aItem in whiteList[aWhite]:
            print(aItem[0])
            print(aItem[1])


def isInBlack(aStr):
    for aItem in blackList:
        if aItem in aStr:
            return True
    return False


with open("cn.m3u", 'r') as fin:
    allLines = fin.readlines()
    fileLength = len(allLines)
    index = 0

    while index < fileLength-1:
        aLine = allLines[index].strip()
        nextLine = allLines[index+1].strip()
        if aLine.startswith("#"):
            if isInBlack(aLine):
                pass
            elif isInWhite(aLine, nextLine):
                pass
        # 避免有多个注释行
        index += 1

printWhite()
