class node:
    def __init__ (self, data = None, nextNode = None):
        self.data = data
        self.next = nextNode
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, nextNode):
        self.next = nextNode

class linkedList:
    

    def __init__(self, data = None):
        head = node(data)
        self.head = head
        self.current = self.head
    
    def insertFront(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode
        self.current = self.head
    
    def insertEnd(self, data):
        newNode = node(data)
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = newNode
        del temp
    
    def reverseList(self):
        temp = self.head
        self.head = self.head.next
        temp2 = self.head.next
        temp.next = None
        while(temp2):
            self.head.next = temp
            temp = self.head
            self.head = temp2
            temp2 = self.head.next
        self.head.next = temp
        self.current = self.head
    
    def __iter__ (self):
        return self
    
    def __next__ (self):
        if(self.current == None):
            self.current = self.head
            raise StopIteration
        temp = self.current
        self.current = self.current.next
        return temp
    
lis = linkedList(2)
lis.insertFront(1)
lis.insertEnd(3)
for i in lis:
    print(i.data)
lis.reverseList()
for i in lis:
    print(i.data)