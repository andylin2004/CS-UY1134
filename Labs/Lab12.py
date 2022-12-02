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