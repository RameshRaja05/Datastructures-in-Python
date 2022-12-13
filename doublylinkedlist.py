class DoublyLinkedList():
    def __init__(self, value):
        self.head = {'value': value, 'next': None,'prev':None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newnode = {'value': value, 'next': None,'prev':None}
        self.tail['next'] = newnode
        newnode['prev']=self.tail
        self.tail = newnode
        self.length += 1

    def prepend(self, value):
        newnode = {'value': value, 'next': None,'prev':None}
        newnode['next'] = self.head
        self.head = newnode
        self.length += 1

    def printlist(self):
        curnode = self.head
        lis = []
        while (curnode is not None):
            lis.append(curnode['value'])
            curnode = curnode['next']
        return lis

    def insert(self, index, value):
        if (index <= 0):
            return self.prepend(value)
        elif (index >= self.length):
            return self.append(value)
        headernode = self.traversaltoindex(index-1)
        newnode = {'value': value, 'next': None,'prev':None}
        holdingvalue = headernode['next']
        newnode['prev']=headernode
        headernode['next'] = newnode
        holdingvalue['prev']=newnode
        newnode['next'] = holdingvalue
        self.length += 1

    def traversaltoindex(self, index):
        counter = 0
        curnode = self.head
        while (counter != index):
            counter += 1
            curnode = curnode['next']
        return curnode

    def removebyindex(self, index):
        header = self.traversaltoindex(index-1)
        unwantedvalue = header['next']
        nextvalue=unwantedvalue['next']

        header['next'] = nextvalue
        nextvalue['prev']=header
        self.length -= 1
        return self.printlist()

    def removebyValue(self, value):
        find = False
        indexvalue = -1
        curnode = self.head
        while (not find):
            if (curnode['value'] == value):
                find = True
            curnode = curnode['next']
            indexvalue += 1
        self.removebyindex(indexvalue)
        self.length -= 1
        return self.printlist()


mylinkedlist = DoublyLinkedList(10)
mylinkedlist.append(20)
mylinkedlist.append(30)
mylinkedlist.append(40)
mylinkedlist.append(50)
mylinkedlist.prepend(9)
mylinkedlist.prepend(8)
mylinkedlist.prepend(7)
print(mylinkedlist.removebyindex(2))
mylinkedlist.removebyValue(8)
print(mylinkedlist.printlist())
