from DoublyLinkedList import *

class LinkedQueue:
    def __init__(self) -> None:
        self.queue = DoublyLinkedList()

    def __len__(self):
        return len(self.queue)
    
    def enqueue(self, value):
        self.queue.add_last(value)
    
    def dequeue(self):
        return self.queue.delete_first()
    
    def first(self):
        return self.queue.header.next.data

    def is_empty(self):
        return self.queue.is_empty()

if __name__ == "__main__": 
    lq = LinkedQueue()
    lq.enqueue(0)
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.enqueue(6)
    lq.enqueue(7)
    lq.enqueue(8)
    lq.enqueue(9)
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    print(lq.first())