from BinarySearchTreeMap import *

def create_chain_bst(n):
    bst = BinartSearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i, i)