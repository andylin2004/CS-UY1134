from LinkedBinaryTree import *

def is_height_balanced(bin_tree):
    def subtree_height_measure(root):
        if root is None:
            return (0, True)
        else:
            left_results = subtree_height_measure(root.left)
            right_results = subtree_height_measure(root.right)
            if left_results[1] and right_results[1]:
                return (max(left_results[0], right_results[0]) + 1, abs(left_results[0] - right_results[0]) <= 1)
            else:
                return (0, False)
    
    return subtree_height_measure(bin_tree.root)[1]

if __name__ == "__main__": 
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(4)
    c = LinkedBinaryTree.Node(6, a, b)
    d = LinkedBinaryTree.Node(8)
    e = LinkedBinaryTree.Node(10, None, d)
    f = LinkedBinaryTree.Node(12, e, c)
    bin_tree = LinkedBinaryTree(f)
    print(is_height_balanced(bin_tree))