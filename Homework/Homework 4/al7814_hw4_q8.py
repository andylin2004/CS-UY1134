def flat_list(nested_lst, low, high):
    return_lst = []
    if low < high:
        return_lst = flat_list(nested_lst, low, high-1)
    if isinstance(nested_lst[high], list):
        for i in flat_list(nested_lst[high], 0, len(nested_lst[high]) - 1):
            return_lst.append(i)
    elif isinstance(nested_lst[high], int):
        return_lst.append(nested_lst[high])
    return return_lst
        

if __name__ == "__main__": 
    nested_lst=[[1, 2], 3, [4, [5, 6, [7], 8]]]
    print(flat_list(nested_lst, 0, 2))