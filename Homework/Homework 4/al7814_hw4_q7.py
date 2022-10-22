def split_by_sign(lst, low, high):
    if high - low > 0:
        if lst[low] >= 0 and lst[high] < 0:
            (lst[low], lst[high]) = (lst[high], lst[low])
            split_by_sign(lst, low+1, high-1)
        elif lst[low] < 0:
            split_by_sign(lst, low+1, high)
        elif lst[high] >= 0:
            split_by_sign(lst, low, high-1)

if __name__ == "__main__": 
    lst = [-1, 20, 0, 12, -1, -20, -6, 5]
    split_by_sign(lst, 0, len(lst)-1)
    print(lst)