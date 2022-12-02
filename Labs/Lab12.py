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
    while bst.root is not None and ((bst.root.item.key < n and bst.root.right is not None) or (bst.root.item.key > n and bst.root.left is not None)):
        if bst.root.item.key < n:
            node = node.right
        elif bst.root.item.key > n:
            node = node.left
    return node