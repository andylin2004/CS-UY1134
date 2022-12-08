from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    def recursive_part(node, is_left):
        if node.left is None and node.right is None:
            return (node.item.key)
        else:
            left_side = recursive_part(node.left, True)
            right_side = recursive_part(node.right, False)
            left_diff = abs(node.item.key - left_side[0])
            right_diff = abs(node.item.key - right_side[0])
            min_dif = min(left_diff, right_diff)
            if is_left:
                to_store = right_side[0]
                if len(right_side) >= 3:
                    stored_diff = abs(node.item.key - right_side[2])
                    min_dif = min(min_dif, stored_diff)
            else:
                to_store = left_side[0]
                if len(left_side) >= 3:
                    stored_diff = abs(node.item.key - left_side[2])
                    min_dif = min(min_dif, stored_diff)
            return (node.item.key, min_dif, to_store)
            