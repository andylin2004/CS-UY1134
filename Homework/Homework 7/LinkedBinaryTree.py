from ArrayQueue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    #q2
    
    def leaves_list(self):
        def leaf_finder(root):
            if root.left is None and root.right is None:
                yield root.data
            else:
                if root.left is not None:
                    yield from leaf_finder(root.left)
                if root.right is not None:
                    yield from leaf_finder(root.right)
        
        return [x for x in leaf_finder(self.root)]

    #q4

    def iterative_inorder(self):
        node = self.root
        counter = 0
        reverse = False
        if node is None:
            raise Exception()
        while counter < len(self):
            if reverse:
                while node.right is None:
                    node = node.parent
                node = node.right
                reverse = False
            else:
                if node.left is None and node.right is None:
                    yield node.data
                    node = node.parent
                    yield node.data
                    if node.right is not None:
                        node = node.right
                    else:
                        node = node.parent
                        reverse = True
                elif node.left is not None:
                    node = node.left
                else:
                    yield node.data
                    if node.right is not None:
                        node = node.right
                    else:
                        node = node.parent
                        reverse = True

if __name__ == "__main__": 
    n1 = LinkedBinaryTree.Node(5)
    n2 = LinkedBinaryTree.Node(1)
    n3 = LinkedBinaryTree.Node(9, n1, n2)
    n4 = LinkedBinaryTree.Node(2, n3)
    n5 = LinkedBinaryTree.Node(8)
    n6 = LinkedBinaryTree.Node(4)
    n7 = LinkedBinaryTree.Node(7, n5, n6)
    n8 = LinkedBinaryTree.Node(3, n4, n7)
    lb = LinkedBinaryTree(n8)
    for i in lb.iterative_inorder():
        print(i)


