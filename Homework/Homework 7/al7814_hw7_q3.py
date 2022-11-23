from math import max, abs

def is_height_balanced(bin_tree):
    def subtree_height_measure(root):
        if root is None:
            return (0, True)
        else:
            left_results = subtree_height_measure(root.left)
            right_results = subtree_height_measure(root.right)
            if left_results[1] and right_results[1]:
                return (max(left_results[0], right_results[0]), abs(left_results[0] - right_results[0]) <= 1)
            else:
                return (0, False)