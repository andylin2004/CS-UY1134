from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    def recursive_part(node, is_left):
        if node is None:
            return None
        else:
            left_side = recursive_part(node.left, True)
            right_side = recursive_part(node.right, False)
            min_dif = None
            if left_side is not None:
                left_diff = abs(node.item.key - left_side[0])
                min_dif = left_diff
                if left_side[1] is not None:
                    min_dif = min(min_dif, left_side[1])
            if right_side is not None:
                right_diff = abs(node.item.key - right_side[0])
                if min_dif is None:
                    min_dif = right_diff
                else:
                    min_dif = min(min_dif, right_diff)
                if right_side[1] is not None:
                    min_dif = min(min_dif, right_side[1])
            to_store = None
            if is_left and right_side is not None:
                to_store = right_side[0]
                if right_side[2] is not None:
                    stored_diff = abs(node.item.key - right_side[2])
                    min_dif = min(min_dif, stored_diff)
            elif left_side is not None:
                to_store = left_side[0]
                if left_side[2] is not None:
                    stored_diff = abs(node.item.key - left_side[2])
                    min_dif = min(min_dif, stored_diff)
            return (node.item.key, min_dif, to_store)
            
    return recursive_part(bst.root, False)[1]

if __name__ == "__main__": 
    from al7814_hw8_q3 import *
    bst = BinarySearchTreeMap()
    bst.insert(9,1)
    bst.insert(7,1)
    bst.insert(20,1)
    bst.insert(4,1)
    bst.insert(1,1)
    bst.insert(6,1)
    bst.insert(17,1)
    bst.insert(25,1)
    print([x.item.key for x in bst.inorder()])
    print(find_min_abs_difference(bst))
    bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
    print(find_min_abs_difference(bst))