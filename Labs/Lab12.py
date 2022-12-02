from ArrayQueue import *

#q1
def min_max_BST(bst):
    ''' Returns a tuple containing the min and max keys in the
    binary search tree'''
    left = bst.root
    right = bst.root
    while left.left is not None:
        left = left.left
    while right.right is not None:
        right = right.right
    return (left.item.key, right.item.key)

#q2
def glt_n(bst, n): #glt = greatest less than
    ''' Returns the greatest number in the binary search tree
    less than or equal to n'''
    node = bst.root
    while bst.root is not None and bst.root.item.key != n and ((bst.root.item.key < n and bst.root.right is not None) or (bst.root.item.key > n and bst.root.left is not None)):
        if bst.root.item.key < n:
            node = node.right
        elif bst.root.item.key > n:
            node = node.left
    return node

#q3
def compare_BST(bst1, bst2):
    ''' Returns true if the two binary search trees contain the
    same set of elements and false if not'''
    def recursive_item_collector(root):
        if root is None:
            return []
        else:
            left_result = recursive_item_collector(root.left)
            right_result = recursive_item_collector(root.right)
            return left_result + right_result + [root.item]
        
    for i in recursive_item_collector(bst1):
        if bst2.find_node(i.key).item.value != i.value:
            return False
    return True