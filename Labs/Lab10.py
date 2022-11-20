from DoublyLinkedList import *

# q1

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)

    def is_empty(self):
        ''' Returns true if the stack is empty,false otherwise. '''
        return self.data.is_empty()

    def push(self, e):
        ''' Adds an element, e, to the top of the stack. '''
        self.data.add_first(e)

    def top(self):
        ''' Returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception()
        else:
            return self.data.header.next.data

    def pop(self):
        ''' Removes and returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception()
        else:
            return self.data.delete_first()

# q3

class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None

    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)

    def is_empty(self):
        ''' Returns true if stack is empty and false otherwise. '''
        return self.data.is_empty()

    def push(self, e):
        ''' Adds an element, e, to the top of the stack. '''
        self.data.add_first(e)
        if len(self) == 1:
            self.mid = self.data.header.next
        elif len(self) % 2 == 1:
            self.mid = self.mid.prev

    def top(self):
        ''' Returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception()
        else:
            return self.data.header.next.data

    def pop(self):
        ''' Removes and returns the element at the top of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception()
        else:
            if len(self) == 1:
                self.mid = None
            elif len(self) % 2 == 1:
                self.mid = self.mid.prev
            return self.data.delete_first()

    def mid_push(self, e):
        ''' Adds an element, e, to the middle of the stack.
        An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception()
        else:
            self.mid = self.data.add_after(self.mid, e)
            
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