from math import min, max

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root is None:
            return None
        else:
            left_minmax = subtree_min_and_max(root.left)
            right_minmax = subtree_min_and_max(root.right)
            if left_minmax is None and right_minmax is None:
                return (root.data, root.data)
            elif left_minmax is None:
                grand_min = min(root.data, right_minmax[0])
                grand_max = max(root.data, right_minmax[1])
                return (grand_min, grand_max)
            elif right_minmax is None:
                grand_min = min(root.data, left_minmax[0])
                grand_max = max(root.data, left_minmax[1])
                return (grand_min, grand_max)
            else:
                grand_min = min(left_minmax[0], right_minmax[0], root.data)
                grand_max = max(left_minmax[1], right_minmax[1], root.data)
                return (grand_min, grand_max)

    return subtree_min_and_max(bin_tree.root)