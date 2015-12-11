
def changeTimeCharToInt(timedata):
    timedataList = timedata.split(",")
    timeIntVersion = [sumTimeInteager(timedataList[0])]

    for i in range (1, len(timedataList)):
        if(timedataList[i - 1][0] != timedataList[i][0]):
            timeIntVersion.append(sumTimeInteager(timedataList[i]))
        else:
            temp = timeIntVersion[len(timeIntVersion) - 1]

            timeIntVersion[len(timeIntVersion) - 1] = (temp | sumTimeInteager(timedataList[i]))

    print(timeIntVersion)


def returnDayToInt(ch):
    if ch == '월':
        return 0x80000000
    elif ch == '화':
        return 0x40000000
    elif ch == '수':
        return 0x20000000
    elif ch == '목':
        return 0x10000000
    elif ch == '금':
        return 0x08000000

def returnTimeToInt(char):
    if char.isdigit():
        bitmask = 0x00030000
        for i in range (1, 10):
            if i == int(char):
                return bitmask
            bitmask >>= 2

    else:
        bitmask = 0x00038000
        for i in range(ord('A'), ord('G')):
            if chr(i) == char:
                return bitmask
            bitmask >>= 3

def sumTimeInteager(string):
    return (returnDayToInt(string[0]) | returnTimeToInt(string[1]))
