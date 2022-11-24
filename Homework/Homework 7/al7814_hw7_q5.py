from LinkedBinaryTree import *

def create_expression_tree(prefix_exp_str):
    tokens = prefix_exp_str.split()
    def create_expression_tree_helper(start_pos):
        node = LinkedBinaryTree.Node(tokens[start_pos])
        start_pos += 1
        if tokens[start_pos].isnumeric():
            node.left = LinkedBinaryTree.Node(int(tokens[start_pos]))
            start_pos += 1
        else:
            subexp_result = create_expression_tree_helper(start_pos)
            node.left = subexp_result[0]
            start_pos = subexp_result[1]
        if tokens[start_pos].isnumeric():
            node.right = LinkedBinaryTree.Node(int(tokens[start_pos]))
            start_pos += 1
        else:
            subexp_result = create_expression_tree_helper(start_pos)
            node.right = subexp_result[0]
            start_pos = subexp_result[1]
        return (node, start_pos)

    return create_expression_tree_helper(0)[0]
