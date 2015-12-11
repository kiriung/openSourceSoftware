from copy import copy

data = [{'name':'math', 'class':1, 'time': [0x80004000, 0x20000E00]}, {'name':'math', 'class':2, 'time': [0x80000E00, 0x20004000]}, {'name':'computer', 'class':1, 'time': [0x40000038, 0x100001C0]}, {'name':'computer', 'class':2, 'time':[0x400001C0, 0x10000038]}
    ,{'name':'statics', 'class':1, 'time':[0x40000007, 0x10000007]}, {'name':'statics', 'class' : 2, 'time':[0x40000E00, 0x10007000]}]

class Node:
    def __init__(self,dict):
        self.name = dict['name']
        self.time = dict['time']
        self.divClass = dict['class']
        self.next = []

    def addList(self, leaf):
        self.next.append(leaf)

def compareTime(parent, child):
    for i in parent.time:
        for j in child.time:
            isSameTime = i & j
            if (isSameTime & 0x0003FFFF != 0) and (isSameTime & 0xF1000000 != 0):
                return False

    return True

def saveTimeTable(node):
    if len(node.next) == 0:
        return None
    else:
        for i in node.next:
            return saveTimeTable(i)

root = []
name = data[0]['name']

for i in range(0, len(data)):
    while name == data[i]['name']:
        node = Node(data[i])
        root.append(node)
        i += 1
    break

parentNodeList = []
childNodeList = []

for i in range(len(root), len(data)):
    if i == len(root):
        parentNodeList = root

    else:
        tempList = []
        for k in parentNodeList:
            for j in range(0, len(parentNodeList)):
                tempList.append(parentNodeList[j].next)

    name = copy(data[i]['name'])

    while name == data[i]['name']:
        node = Node(data[i])
        childNodeList.append(node)
        i += 1
        if(i == len(data)):
            break

    i -= 1

    for k in parentNodeList:
        for j in childNodeList:
            if compareTime(k, j):
                k.addList(j)
