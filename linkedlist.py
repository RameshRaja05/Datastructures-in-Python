class LinkedList():
    def __init__(self, value):
        self.head = {'value': value, 'next': None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newnode = {'value': value, 'next': None}
        self.tail['next'] = newnode
        self.tail = newnode
        self.length += 1

    def prepend(self, value):
        newnode = {'value': value, 'next': None}
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
        newnode = {'value': value, 'next': None}
        holdingvalue = headernode['next']
        headernode['next'] = newnode
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
        header['next'] = unwantedvalue['next']
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
    def reverse(self):
        prev=None #we created a prev var in order to reverse a linked list first ele becomes last eele in ll last ele point to null
        cur=self.head #first ele
        while(cur):#it keeps run untill it get end of ll
            nxt=cur['next'] #we gonna change a cur value to null this is why we don't wanna lose a next value
            cur['next']=prev #first value of next points null
            prev=cur#prev becomes first value
            cur=nxt #change the cur value to next value
        return prev
    


mylinkedlist = LinkedList(10)
mylinkedlist.append(20)
mylinkedlist.append(30)
mylinkedlist.append(40)
mylinkedlist.append(50)
mylinkedlist.prepend(9)
mylinkedlist.prepend(8)
mylinkedlist.prepend(7)
mylinkedlist.removebyindex(2)
mylinkedlist.removebyValue(8)
print(mylinkedlist.printlist())
print(mylinkedlist.reverse())
