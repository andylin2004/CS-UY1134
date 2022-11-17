from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    new_list = DoublyLinkedList()
    for i in lnk_lst:
        new_list.add_last(i)
    return new_list

if __name__ == "__main__":
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)
    lnk_lst2 = copy_linked_list(lnk_lst1)
    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)