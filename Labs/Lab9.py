from ArrayQueue import *
import ctypes  # provides low-level arrays

# q1

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

# q2

def flatten_list_by_depth(lst): 
    """
    : lst type: list
    : return type: list
    """
    q = ArrayQueue()
    new_lst = []
    ''' Remove and return the top element from the stack. If the
    stack is empty, raise an exception'''
    for i in lst:
        q.enqueue(i)
    while not q.is_empty():
        if isinstance(q.first(), list):
            total = len(q) - 1
            for i in q.dequeue():
                q.enqueue(i)
            for _ in range(total):
                q.enqueue(q.dequeue())
        else:
            new_lst.append(q.dequeue())
    return new_lst

# q3

def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue_last(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[2] = elem
            self.front_ind = 2
            self.back_ind = 2
            self.n += 1
        else:
            self.back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[self.back_ind] = elem
            self.n += 1

    def enqueue_first(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if self.is_empty():
            self.data_arr[2] = elem
            self.front_ind = 2
            self.back_ind = 2
            self.n += 1
        else:
            self.front_ind = (self.back_ind - self.n) % self.capacity
            self.data_arr[self.front_ind] = elem
            self.n += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % self.capacity
        self.n -= 1
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        offset = (new_cap - len(self.data_arr)) // 2
        for new_ind in range(self.n):
            new_data[new_ind + offset] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0

# q4

class QueueStack_fastpush:
    def __init__(self):
        self.data = ArrayQueue()
        self.first_in_front = False

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        ''' Add element e to the top of the stack '''
        self.first_in_front = False
        self.data.enqueue(e)

    def pop(self):
        ''' Remove and return the top element from the stack. If the stack is empty, raise an exception'''
        if not self.first_in_front:
            for _ in range(len(self.data) - 1):
                self.data.enqueue(self.data.dequeue())
        self.first_in_front = False
        return self.data.dequeue()

    def top(self):
        ''' Return a reference to the top element of the stack without removing it. If the stack is empty, raise an exception '''
        if not self.first_in_front:
            for _ in range(len(self.data) - 1):
                self.data.enqueue(self.data.dequeue())
        self.first_in_front = True
        return self.data.first()

class QueueStack_fastpoptop:
    def __init__(self):
        self.data = ArrayQueue()
        self.first_in_front = False

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        ''' Add element e to the top of the stack '''
        self.data.enqueue(e)
        for _ in range(len(self.data) - 1):
            self.data.enqueue(self.data.dequeue())

    def pop(self):
        ''' Remove and return the top element from the stack. If the stack is empty, raise an exception'''
        return self.data.dequeue()

    def top(self):
        ''' Return a reference to the top element of the stack without removing it. If the stack is empty, raise an exception '''
        return self.data.first()

if __name__ == "__main__": 
    lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
    new_lst = flatten_list_by_depth(lst)
    print(new_lst)
    print()

    dq = ArrayDeque()
    dq.enqueue_first(0)
    dq.enqueue_first(1)
    dq.enqueue_last(2)
    dq.enqueue_last(3)
    print(dq.dequeue_first())
    print(dq.dequeue_first())
    dq.enqueue_first(11)
    dq.enqueue_first(12)
    dq.enqueue_first(13)
    dq.enqueue_first(14)
    print(dq.dequeue_first())
    print(dq.dequeue_first())
    print(dq.dequeue_first())
    print(dq.dequeue_first())
    print(dq.dequeue_last())
    dq.enqueue_last(15)
    dq.enqueue_last(16)
    print(dq.dequeue_last())
    print(dq.dequeue_last())

    print()

    qs = QueueStack_fastpush()
    qs.push(1)
    qs.push(2)
    qs.push(3)
    qs.push(4)
    qs.push(5)
    qs.push(6)
    qs.push(7)
    print(qs.top())
    print(qs.pop())
    qs.push(8)
    qs.push(9)
    print(qs.top())
    print(qs.pop())
    print(qs.pop())
    print(qs.pop())
    print(qs.pop())
    print(qs.pop())

    print()

    qs2 = QueueStack_fastpoptop()
    qs2.push(1)
    qs2.push(2)
    qs2.push(3)
    qs2.push(4)
    qs2.push(5)
    qs2.push(6)
    qs2.push(7)
    print(qs2.data.first())
    print(qs2.top())
    print(qs2.pop())
    print(qs2.pop())
    print(qs2.pop())
    print(qs2.pop())