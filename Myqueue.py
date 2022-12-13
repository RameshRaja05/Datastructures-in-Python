class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    def peek(self):
        return self.first.value
    def enqueue(self,value):
        newnode=node(value)
        if(self.length==0):
            self.first=newnode
            self.last=newnode
        else:
            self.last.next=newnode
            self.last=newnode
        self.length+=1
    def dequeue(self):
        if(not self.first):
            return None
        if(self.first==self.last):
            self.last=None
        unwanted=self.first
        self.first=unwanted.next
        self.length-=1
myqueue=Queue()
myqueue.enqueue(5)
myqueue.enqueue(25)
myqueue.enqueue(50)
myqueue.enqueue(2500)
print(myqueue.length)
myqueue.dequeue()
print(myqueue.length)

    