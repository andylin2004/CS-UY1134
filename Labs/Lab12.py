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
    
    if len(bst1) != len(bst2):
        return False
    else:
        for i in recursive_item_collector(bst1):
            if bst2.find_node(i.key).item.value != i.value:
                return False
        return True

# q4

def is_BST(root):
    def is_BST_helper(root):
        ''' Returns a tuple (min, max, bool)'''
        if root is None:
            return None
        else:
            min_val = root.data
            max_val = root.data
            correct_ordering = True
            left_result = is_BST_helper(root.left)
            right_result = is_BST_helper(root.right)
            if left_result is not None:
                min_val = min(left_result[0], min_val)
                max_val = max(left_result[1], max_val)
                correct_ordering = root.left.data < root.data
            if right_result is not None:
                min_val = min(right_result[0], min_val)
                max_val = max(right_result[1], max_val)
                correct_ordering = correct_ordering and root.data < root.right.data
            return (min_val, max_val, correct_ordering)

    return is_BST_helper(root)[2]