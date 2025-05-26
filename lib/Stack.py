class Stack:
    
    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items
        self.list = items if items else []
        
        
    def isEmpty(self):
        return len(self.list) == 0

    def push(self, item):
        if len(self.list) >= self.limit:
             raise Exception("Stack overflow: Cannot push item, stack is full.")
        self.list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty: Cannot peek.")
        return self.list[-1]
        
    def size(self):
        return len(self.list)

    def full(self):
        return len(self.list) >= self.limit

    def search(self, target):
        if target in self.list:
            return len(self.list) -1- self.list.index(target)
        return -1