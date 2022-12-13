class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None#//equals to null coz we are able to create empty stack
        self.bottom = None#//it looks confusing in stack we wanna keep track our value
        self.length = 0#/empty stack

    def peek(self):#//this means lookup the top value
        return self.top.value

    def push(self, value):
        newnode = node(value)#instantiates node class we can't dry
        if self.length == 0:#if stack is empty
            self.top = newnode#value will be stored right on the top value no need to manipulate the pointer
            self.botton = newnode#it helpful to keep track
        else:
            holdingpointer = self.top#if stack is not empty if we changes top value to new value we will lose a existing values this we stored it on the holdingpointer

            self.top = newnode#new values stored on the top
            newnode.next = holdingpointer#we connected to the existing value
        self.length += 1#increase the length
        return self#we can see our values

    def pop(self):
        if (not self.top): #if stack is empty we return null
            return None
        if (self.top == self.bottom):#if we get a end of stack bottom value changes to null however we don't have values
            self.bottom = None
        unwanted = self.top#let's grab a our value it will be useful to makesure we deleted the top value
        self.top = unwanted.next#top value changes next value
        self.length -= 1#decrease the length
        return unwanted#we can see our del value


mystack = stack()
mystack.push(10)
mystack.push(100)
mystack.push(1000)
mystack.push(10000)
mystack.push(100000)
print(mystack.peek())
mystack.pop()
print(mystack.peek())
print(mystack.push(101))