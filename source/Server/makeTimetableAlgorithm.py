data = [{'name':'math', 'class':1, 'time': 0x00000011}, {'name':'math', 'class':2, 'time': 0x00001100}, {'name':'computer', 'class':1, 'time': 0x000110000}, {'name':'computer', 'class':2, 'time':0x00001100}]

class Node:
    def __init__(self,dict):
        self.name = dict['name']
        self.time = dict['time']
        self.divClass = dict['class']
        self.next = []

    def addList(self, leaf):
        self.next.append(leaf)

def compareTime(parent, child):
    if parent.time & child.time != 0:
        return True
    else:
        return False

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
            for j in parentNodeList[k].next:
                tempList.append(j)

    name = data[i]['name']

    while name == data[i]['name']:
        node = Node(data[i])
        childNodeList.append(node)
        i += 1

    i -= 1

    for k in parentNodeList:
        for j in childNodeList:
            if compareTime(k, j):
                k.addList(j)


