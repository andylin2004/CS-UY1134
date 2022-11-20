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

def bt_contains(root, val):
    ''' Returns True if val exists in the binary tree and
    false if not'''
    if root is None:
        return False
    else:
        return root.data == val or bt_contains(root.left, val) or bt_contains(root.right, val)

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