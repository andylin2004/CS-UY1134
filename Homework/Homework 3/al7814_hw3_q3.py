def find_duplicates(lst):
    num_found = [0] * len(lst)

    for i in lst:
        num_found[i] += 1
    
    return_arr = []

    for i in range(len(num_found)):
        if num_found[i] > 1:
            return_arr.append(i)
    
    return return_arr

if __name__ == "__main__":
    lst = [2,4,4,1,2]
    print(find_duplicates(lst))
