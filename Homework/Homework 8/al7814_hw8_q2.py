from BinarySearchTreeMap import *

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i, i)

def add_items(bst, low, high):
    mid = (high + low) // 2
    bst.insert(mid, mid)
    if high-low > 1:
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)
        
def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

if __name__ == "__main__": 
    print(create_complete_bst(7))