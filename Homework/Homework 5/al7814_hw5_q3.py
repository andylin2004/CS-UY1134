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
    
    def push(self, e):
        if len(self.stack) < len(self.deque):
            self.stack.push(self.deque.dequeue_first())
        self.deque.enqueue_last(e)
    
    def mid_push(self, e):
        if len(self.stack) < len(self.deque):
            self.stack.push(self.deque.dequeue_first())
        self.deque.enqueue_first(e)
    
    def top(self):
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.deque.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            popped = self.deque.dequeue_last()
            if not self.stack.is_empty():
                self.deque.enqueue_first(self.stack.pop())
            return popped

if __name__ == "__main__": 
    mids = MidStack ()
    mids.push (2)
    mids.push (4)
    mids.push (6)
    mids.push (8)
    mids.mid_push(10)
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop()) 
    print(mids.pop())
    print()
    mids = MidStack ()
    mids.push(2)
    mids.push(4)
    mids.push(6)
    mids.push(8)
    mids.push(10)
    mids.mid_push(12)
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())