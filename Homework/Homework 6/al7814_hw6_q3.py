from DoublyLinkedList import *

class CompactString:
    def __init__(self, orig_str):
        ''' Initializes a CompactString object representing the string given in orig_str'''
        self.linked_list = DoublyLinkedList()
        if orig_str is not None:
            currently_repeating_char = None
            total = 0
            for i in orig_str:
                if currently_repeating_char is not None:
                    if i != currently_repeating_char:
                        self.linked_list.add_last((currently_repeating_char, total))
                        total = 0
                currently_repeating_char = i
                total += 1
            self.linked_list.add_last((currently_repeating_char, total))

    def __add__(self, other):
        ''' Creates and returns a CompactString object that represent the concatenation of self and other,
        also of type CompactString'''
        new_compact = CompactString(None)
        for i in self.linked_list:
            new_compact.linked_list.add_last(i)
        for i in other.linked_list:
            if new_compact.linked_list.trailer.prev.data[0] == i[0]:
                removed_from_last = new_compact.linked_list.delete_last()
                new_compact.linked_list.add_last((removed_from_last[0], removed_from_last[1] + i[1]))
            else:
                new_compact.linked_list.add_last(i)
        return new_compact

    def __lt__(self, other):
        ''' returns True if”f self is lexicographically less than other, also of type CompactString'''
    def __le__(self, other):
        ''' returns True if”f self is lexicographically less than or equal to other, also of type CompactString'''
    def __gt__(self, other):
        ''' returns True if”f self is lexicographically greater than other, also of type CompactString'''
    def __ge__(self, other):
        ''' returns True if”f self is lexicographically greater than or equal to other, also of type CompactString'''
    def __repr__(self):
        ''' Creates and returns the string representation (of type str) of self'''

if __name__ == "__main__": 
    compact_string = CompactString("aaaaabbbaaac")
    print(compact_string.linked_list)
    compact_2 = CompactString("aaaaaaacccaaaa")
    compact_sum = compact_2 + compact_string
    print(compact_sum.linked_list)