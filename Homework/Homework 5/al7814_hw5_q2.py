from ArrayStack import *

class MaxStack:
    def __init__(self) -> None:
        self.stack = ArrayStack()
        self.max_value = 0
    
    def is_empty(self):
        return self.stack.is_empty()
    
    def __len__(self):
        return len(self.stack)
    
    def push(self, e):
        self.stack.push(e)
    
    def top(self):
        return self.stack.top()
    
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        else:
            return self.stack.pop()