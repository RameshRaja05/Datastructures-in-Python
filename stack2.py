class stack:
    def __init__(self):
        self.array=[]
    def push(self,value):
        self.array.append(value)
        return self
    def pop(self):
        self.array.pop()
    def peek(self):
        return self.array[len(self.array)-1]
mystack=stack()
mystack.push(10)
mystack.push(100)
mystack.push(1000)
mystack.push(10000)
print(mystack.peek())
mystack.pop()
mystack.pop()
mystack.pop()
print(mystack.peek())