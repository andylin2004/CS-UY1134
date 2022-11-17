from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(lst1_pointer, lst2_pointer, doubly_list):
        if lst1_pointer.data is not None and lst2_pointer.data is not None:
            if lst1_pointer.data <= lst2_pointer.data:
                doubly_list.add_last(lst1_pointer.data)
                return merge_sublists(lst1_pointer.next, lst2_pointer, doubly_list)
            else:
                doubly_list.add_last(lst2_pointer.data)
                return merge_sublists(lst1_pointer, lst2_pointer.next, doubly_list)
        elif lst1_pointer.data is not None:
            doubly_list.add_last(lst1_pointer.data)
            return merge_sublists(lst1_pointer.next, lst2_pointer, doubly_list)
        elif lst2_pointer.data is not None:
            doubly_list.add_last(lst2_pointer.data)
            return merge_sublists(lst1_pointer, lst2_pointer.next, doubly_list)
        else:
            return doubly_list 

    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, DoublyLinkedList())

if __name__ == "__main__": 
    srt_lnk_lst1 = DoublyLinkedList()
    srt_lnk_lst1.add_last(1)
    srt_lnk_lst1.add_last(3)
    srt_lnk_lst1.add_last(5)
    srt_lnk_lst1.add_last(6)
    srt_lnk_lst1.add_last(8)
    srt_lnk_lst2 = DoublyLinkedList()
    srt_lnk_lst2.add_last(2)
    srt_lnk_lst2.add_last(3)
    srt_lnk_lst2.add_last(5)
    srt_lnk_lst2.add_last(10)
    srt_lnk_lst2.add_last(15)
    srt_lnk_lst2.add_last(18)
    print(merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2))