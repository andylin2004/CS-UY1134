from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    new_list = DoublyLinkedList()
    for i in lnk_lst:
        new_list.add_last(i)

