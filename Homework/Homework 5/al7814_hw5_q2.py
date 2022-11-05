from ArrayStack import *

class MaxStack:
    def __init__(self) -> None:
        self.stack = ArrayStack()
        self.max_value = 0
    
    def is_empty(self):
        return self.stack.is_empty()
    
    def __len__(self):
        return len(self.stack)