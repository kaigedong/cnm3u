
whiteList = {}
blackList = {}

# 读取白名单
with open("whitelist.txt", 'r') as fin:
    for aline in fin:
        aline = aline.strip()
        if aline != "":
            whiteList[aline] = 1
# 读取黑名单
with open("blacklist.txt", "r") as fin:
    for aline in fin:
        aline = aline.strip()
        if aline != "":
            blackList[aline] = 1


def isInWhite(aStr):
    for aItem in whiteList:
        if aItem in aStr:
            return True
    return False


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
            elif isInWhite(aLine):
                print(aLine)
                print(nextLine)
        # 避免有多个注释行
        index += 1
