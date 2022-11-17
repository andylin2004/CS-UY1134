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
        return self.queue.first()

    def is_empty(self):
        return self.queue.is_empty()