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
        if self.max_value < e:
            self.stack.push((e, self.max_value))
            self.max_value = e
        else:
            self.stack.push((e, None))
    
    def top(self):
        return self.stack.top()[0]
    
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        else:
            popped = self.stack.pop()
            if popped[1] != None:
                self.max_value = popped[1]
            return popped[0]