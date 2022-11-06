from ArrayStack import *
from ArrayDeque import *

class MidStack:
    def __init__(self) -> None:
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def is_empty(self):
        return self.stack.is_empty() and self.deque.is_empty()
    
    def __len__(self):
        return len(self.stack) + len(self.deque)