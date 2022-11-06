from ArrayStack import *

class Queue:
    def __init__(self) -> None:
        self.stack_1 = ArrayStack()
        self.stack_2 = ArrayStack()
        self.stack_used = 1

    def is_empty(self):
        if self.stack_used == 1:
            return self.stack_1.is_empty()
        else:
            return self.stack_2.is_empty()

    def __len__(self):
        if self.stack_used == 1:
            return len(self.stack_1)
        else:
            return len(self.stack_2)

    def enqueue(self, item):
        if self.stack_used == 2:
            self.stack_used = 1
            for _ in range(len(self.stack_2)):
                self.stack_1.push(self.stack_2.pop())
        self.stack_1.push(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.stack_used == 1:
            self.stack_used = 2
            for _ in range(len(self.stack_1)):
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            if self.stack_used == 1:
                for _ in range(len(self.stack_1) - 1):
                    self.stack_2.push(self.stack_1.pop())
            return self.stack_2.top()

if __name__ == "__main__": 
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())