class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.left_child_count = 0
            self.right = None
            self.right_child_count = 0

        def num_children(self):
            count = 0
            if(self.left is not None):
                count += 1
            if(self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.right_child_count = None
            self.left_child_count = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)


    # returns value, or raises exception if not found
    def __getitem__(self, key):
        node = self.find_node(key)
        if(node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # return node with key, or None if not found
    def find_node(self, key):
        cursor = self.root
        while(cursor is not None):
            if(cursor.item.key == key):
                return cursor
            elif(cursor.item.key > key):
                cursor = cursor.left
            else: # (cursor.item.key < key
                cursor = cursor.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.find_node(key)
        if(node is not None):
            node.item.value = value
        else:
            self.insert(key, value)

    # assumes that key is not in the tree
    def insert(self, key, value):
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        if(self.is_empty() == True):
            self.root = new_node
            self.n = 1
        else:
            parent = None
            cursor = self.root
            while(cursor is not None):
                parent = cursor
                if(key < cursor.item.key):
                    cursor.left_child_count += 1
                    cursor = cursor.left
                else:
                    cursor.right_child_count += 1
                    cursor = cursor.right
            if(key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.n += 1


    # raises an exceprion if ket not in the tree
    def __delitem__(self, key):
        node = self.find_node(key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            self.delete_node(node)

    # assumes the key is in the tree + returns item that was removed from the tree
    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()

        if(node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.n -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                    self.root.left_child_count -= 1
                else:
                    self.root = self.root.right
                    self.root.right_child_count -= 1
                self.root.parent = None
                node_to_delete.disconnect()
                self.n -= 1

            else:  # num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)

        else:
            if(num_children == 0):
                parent = node_to_delete.parent
                if(node_to_delete is parent.left):
                    parent.left = None
                    parent.left_child_count -= 1
                else:
                    parent.right = None
                    parent.right_child_count -= 1

                node_to_delete.disconnect()
                self.n -= 1

            elif(num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                if(node_to_delete is parent.left):
                    parent.left = child
                    parent.left_child_count -= 1
                else:
                    parent.right = child
                    parent.right_child_count -= 1
                child.parent = parent

                node_to_delete.disconnect()
                self.n -= 1

            else: #(num_children == 2)
                max_in_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_in_left.item
                self.delete_node(max_in_left)

        return item

    def subtree_max(self, subtree_root):
        cursor = subtree_root
        while(cursor.right is not None):
            cursor = cursor.right
        return cursor


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                return
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def preorder(self):
        def subtree_inorder(root):
            if (root is None):
                return
            else:
                yield root
                yield from subtree_inorder(root.left)
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)
    
    def get_ith_smallest(self, i):
        def recursive_part(node, indice):
            if indice <= node.left_child_count:
                return recursive_part(node.left, indice)
            elif indice == node.left_child_count + 1:
                return node.item.key
            else:
                return recursive_part(node.right, indice - 1 - node.left_child_count)

        if i > self.n:
            raise IndexError("Out of bounds")
        else:
            return recursive_part(self.root, i)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key

if __name__ == "__main__":
    bst = BinarySearchTreeMap()
    bst[7] = None
    bst[5] = None
    bst[1] = None
    bst[14] = None
    bst[10] = None
    bst[3] = None
    bst[9] = None
    bst[13] = None
    print(bst.get_ith_smallest(3))
    print(bst.get_ith_smallest(6))
    print([x.item.key for x in bst.inorder()])
    del(bst[14])
    print("deleted 14")
    print(bst.find_node(3))
    print([x.item.key for x in bst.inorder()])
    # del(bst[5])
    # print("deleted 5")
    print(bst.find_node(7))
    print([x.item.key for x in bst.inorder()])
    print(bst.get_ith_smallest(3))
    print([x.item.key for x in bst.inorder()])
    print(bst.get_ith_smallest(6))
    del(bst[7])
    print(bst.find_node(5))
    print([x.item.key for x in bst.inorder()])
    print(bst.get_ith_smallest(2))
    print(bst.get_ith_smallest(3))
    print(bst.get_ith_smallest(4))
    print(bst.get_ith_smallest(6))