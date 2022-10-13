def find_duplicates(lst):
    num_found = [0] * len(lst)

    for i in lst:
        num_found[i] += 1
    
    return_arr = []

    for i in num_found:
        if i > 1:
            return_arr.append(i)
    
    return return_arr