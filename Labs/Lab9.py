from ArrayQueue import *

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
    def __len__(self):
        '''Return the number of elements in the queue'''
    def is_empty(self):
        ''' Return True if queue is empty'''
    def enqueue(self, e):
        ''' Add element e to the front of the queue. If e is not an int or float, raise a TypeError '''
    def dequeue(self):
        ''' Remove and return the first element from the queue. If the queue is empty, raise an exception'''
    def first(self):
        ''' Return a reference to the first element of the queue without removing it. If the queue is empty, raise an exception '''
    def sum(self):
        ''' Returns the sum of all values in the queue'''
    def mean(self):
        ''' Return the mean (average) value in the queue'''