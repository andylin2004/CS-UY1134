from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        ''' Initializes an Integer object representing
        the value given in the string num_str'''
        self.linked_list = DoublyLinkedList()
        not_zero = False
        if num_str is not None:
            for char in num_str:
                if char != '0':
                    not_zero = True
                if not_zero:
                    self.linked_list.add_last(int(char))

    def __add__(self, other):
        ''' Creates and returns an Integer object that represent the sum of self and other, also of type Integer'''
        self_cursor = self.linked_list.trailer.prev
        other_cursor = other.linked_list.trailer.prev
        overflow = 0
        new_integer = Integer(None)
        while self_cursor.data is not None or other_cursor.data is not None:
            total = overflow
            if self_cursor.data is not None:
                total += self_cursor.data
            if other_cursor.data is not None:
                total += other_cursor.data
            new_integer.linked_list.add_first(total % 10)
            overflow = total // 10
            if self_cursor.data is not None:
                self_cursor = self_cursor.prev
            if other_cursor.data is not None:
                other_cursor = other_cursor.prev
        if overflow > 0:
            new_integer.linked_list.add_first(overflow)
        return new_integer

    def __repr__(self):
        ''' Creates and returns the string representation
        of self'''
        return "".join([str(x) for x in self.linked_list])

if __name__ == "__main__": 
    integer = Integer("375")
    integer2 = Integer("4029")
    print(integer)
    integer3 = integer + integer2
    print(integer3)
    integer = Integer("007")
    integer2 = Integer("20")
    print(integer + integer2)
    print(integer)