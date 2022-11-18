from ArrayQueue import *

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.total = 0
        
    def __len__(self):
        '''Return the number of elements in the queue'''
        return len(self.data)

    def is_empty(self):
        ''' Return True if queue is empty'''
        return self.data.is_empty()

    def enqueue(self, e):
        ''' Add element e to the front of the queue. If e is not an int or float, raise a TypeError '''
        if isinstance(e, (int, float)):
            self.data.enqueue(e)
            self.total += e
        else:
            raise TypeError("Invalid type")

    def dequeue(self):
        ''' Remove and return the first element from the queue. If the queue is empty, raise an exception'''
        if self.is_empty():
            raise Exception()
        else:
            dequeued = self.data.dequeue()
            self.total -= dequeued
            return dequeued

    def first(self):
        ''' Return a reference to the first element of the queue without removing it. If the queue is empty, raise an exception '''
        if self.is_empty():
            raise Exception()
        else:
            return self.data.first()

    def sum(self):
        ''' Returns the sum of all values in the queue'''
        return self.total

    def mean(self):
        ''' Return the mean (average) value in the queue'''
        return self.total / len(self.data)