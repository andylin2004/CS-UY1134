def list_min(lst, low, high):
    if high-low == 0:
        return lst[high]
    else:
        if lst[high] < lst[low]:
            return list_min(lst, low+1, high)
        else:
            return list_min(lst, low, high-1)

if __name__ == "__main__": 
    lst = [1,2,3,4,5,6]
    print(list_min(lst, 0, len(lst) - 1))
    lst = [2,3,1,1,4,5,6,0]
    print(list_min(lst, 0, len(lst) - 1))