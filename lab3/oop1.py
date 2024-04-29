class Queue:
    size=int(input("Enter the size of Queue:"))
    def __init__(self):
        self.items = []
        

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.insert(0,item)

    def pop(self):
        #if len(self.items) == size:
            return self.items.pop()

e=Queue()
e.insert("hi")
# e.insert(7)

print(e.pop())
