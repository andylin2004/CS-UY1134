from ArrayStack import *

class Queue:
    def __init__(self) -> None:
        self.stack_1 = ArrayStack()
        self.stack_2 = ArrayStack()
        self.stack_used = 1

    def enqueue(self, item):
        if self.stack_used == 1:
            self.stack_1.push(item)
        else:
            self.stack_2.push(item)
    
    def dequeue(self, item):
        if self.stack_used == 1:
            for _ in range(len(self.stack_1) - 1):
                self.stack_2.push(self.stack_1.pop())
            return self.stack_1.pop()
        else:
            for _ in range(len(self.stack_2) - 1):
                self.stack_1.push(self.stack_2.pop())
            return self.stack_2.pop()