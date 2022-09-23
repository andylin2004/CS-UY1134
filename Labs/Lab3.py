# question 1
# part a
def reverse_list(lst):
    """
    : lst type: list[] 
    : return type: None
    """
    for i in range(len(lst)//2):
        tmp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = tmp

list = [1,2,3,4,5,6]
reverse_list(list)
print(list)

# part b
def reverse_list(lst, low = None, high = None):
    """
    : lst type: list[]
    : low, high type: int
    : return type: None
    """
    if low == high == None:
        low = 0
        high = len(lst) - 1
    
    for i in range(low, ((high + 1 - low) // 2) + low):
        tmp = lst[i]
        lst[i] = lst[high+1-i]
        lst[high+1-i] = tmp

list = [1,2,3,4,5,6]
reverse_list(list, 1, 3)
print(list)