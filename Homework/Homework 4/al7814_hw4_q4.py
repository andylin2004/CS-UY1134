def list_min(lst, low, high):
    if high-low == 0:
        return lst[high]
    else:
        if lst[high] < lst[low]:
            return list_min(lst, low+1, high)
        else:
            return list_min(lst, low, high-1)