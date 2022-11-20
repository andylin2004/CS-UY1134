from LinkedBinaryTree import *

def bt_even_sum(root):
    ''' Returns the sum of all even integers in the binary
    tree'''
    if root is None:
        return 0
    else:
        total = 0
        if root.data % 2 == 0:
            total += root.data
        return total + bt_even_sum(root.left) + bt_even_sum(root.right)