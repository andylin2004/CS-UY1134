from BinarySearchTreeMap import *

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()

    def recursive_part(node, cur_indice):
        if prefix_lst[cur_indice] < node.item.key:
            new_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[cur_indice], prefix_lst[cur_indice]))
            node.left = new_node
            if cur_indice + 1 < len(prefix_lst):
                if prefix_lst[cur_indice + 1] < prefix_lst[0]:
                    if prefix_lst[cur_indice + 1] > node.item.key: 
                        recursive_part(node, cur_indice + 1)
                    else:
                        recursive_part(node.left, cur_indice + 1)
                else:
                    recursive_part(bst.root, cur_indice + 1)
        else:
            new_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[cur_indice], prefix_lst[cur_indice]))
            node.right = new_node
            if cur_indice + 1 < len(prefix_lst):
                if prefix_lst[cur_indice + 1] > prefix_lst[0]:
                    if prefix_lst[cur_indice + 1] < node.item.key: 
                        recursive_part(node, cur_indice + 1)
                    else:
                        recursive_part(node.right, cur_indice + 1)
    
    if len(prefix_lst) > 1:
        bst.insert(prefix_lst[0], prefix_lst[0])
        recursive_part(bst.root, 1)
    return bst

if __name__ == "__main__": 
    bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
    print([str(x.item.key) for x in bst.inorder()])