class MyQueue(object):

    def __init__(self):
        self.Spush = []
        self.Spop = []

    def push(self, x):
        return self.Spush.append(x)
        
    def pop(self):
        if not self.Spush and not self.Spop:
            return
        if self.Spop:
            return self.Spop.pop()
        while self.Spush:
            self.Spop.append(self.Spush.pop())
        return self.pop()

    def peek(self):
        element = self.pop()
        if element is not None:
            self.Spop.append(element)
        return element

    def empty(self):
        if not self.Spush and not self.Spop:
            return True
        return False