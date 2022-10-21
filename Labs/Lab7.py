#q1

def split_parity(lst, low, high):
    """
    : lst type: list[int]
    : low, high type: int
    : return type: None
    """
    mid = (low+high)//2
    i1 = low
    i2 = mid
    if high - low > 0:
        split_parity(lst, low, mid)
        split_parity(lst, mid, high)
    while i1 < mid and i2 < high:
        if lst[i1] % 2 == 0 and lst[i2] % 2 == 1:
            (lst[i1], lst[i2]) = (lst[i2], lst[i1])
        else:
            if lst[i1] % 2 == 0:
                i1 += 1
            if lst[i2] % 2 == 1:
                i2 += 1
        