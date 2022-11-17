from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        ''' Initializes an Integer object representing
        the value given in the string num_str'''
        self.linked_list = DoublyLinkedList()
        for char in num_str:
            self.linked_list.add_last(int(char))

    def __add__(self, other):
        ''' Creates and returns an Integer object that represent the sum of self and other, also of type Integer'''
    
    def __repr__(self):
        ''' Creates and returns the string representation
        of self'''
        return "".join([str(x) for x in self.linked_list])

if __name__ == "__main__": 
    integer = Integer("375")
    print(integer)
