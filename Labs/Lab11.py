from LinkedBinaryTree import *

# q1

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

#q2

def bt_contains(root, val):
    ''' Returns True if val exists in the binary tree and
    false if not'''
    if root is None:
        return False
    else:
        return root.data == val or bt_contains(root.left, val) or bt_contains(root.right, val)

#q3

def is_full(root):
    ''' Returns True if the Binary Tree is full and false
    if not '''
    if root.left is None and root.right is None:
        return True
    elif (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return False
    else:
        return is_full(root.left) == is_full(root.right)

if __name__ == "__main__": 
    n1 = LinkedBinaryTree.Node(1)
    n2 = LinkedBinaryTree.Node(2)
    n12 = LinkedBinaryTree.Node(3, n1, n2)
    n3 = LinkedBinaryTree.Node(4)
    n4 = LinkedBinaryTree.Node(5)
    n34 = LinkedBinaryTree.Node(6, n3, n4)
    n_apex = LinkedBinaryTree.Node(7, n12, n34)
    bt = LinkedBinaryTree(n_apex)
    print(bt_contains(n_apex, 0))
    print(bt_contains(n_apex, 1))
    print(bt_even_sum(n_apex))
    print(is_full(n_apex))
    n12.right = None
    print(is_full(n_apex))