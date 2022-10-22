#q1

def split_parity(lst, low, high):
    """
    : lst type: list[int]
    : low, high type: int
    : return type: None
    """
    if high - low > 0:
        if lst[low] % 2 == 1 and lst[high] % 2 == 0:
            (lst[low], lst[high]) = (lst[high], lst[low])
            split_parity(lst,low+1,high-1)
        elif lst[low] % 2 == 0:
            split_parity(lst,low+1,high)
        elif lst[high] % 2 == 1:
            split_parity(lst,low,high-1)

#q2

def nested_sum(lst):
    """
    : lst type: list
    : output type: int
    """
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += nested_sum(i)
        elif isinstance(i, int):
            total += i
    return total
        
if __name__ == "__main__": 
    lst = [4,-5,2,3,-1,-6,7,9,0]
    split_parity(lst, 0, len(lst) - 1)
    print(lst)
    lst = [ [1, 2], 3, [4, [5, 6, [7], 8 ] ] ]
    print(nested_sum(lst))