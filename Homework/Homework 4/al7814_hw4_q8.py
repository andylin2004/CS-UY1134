def flat_list(nested_lst, low, high):
    return_lst = []
    for i in nested_lst:
        if isinstance(i, list):
            for n in flat_list(i, 0, len(i)):
                return_lst.append(n)
        elif isinstance(i, int):
            return_lst.append(i)
    return return_lst
        

if __name__ == "__main__": 
    nested_lst=[[1, 2], 3, [4, [5, 6, [7], 8]]]
    print(flat_list(nested_lst, 0, 2))