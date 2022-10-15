def remove_all(lst, item):
    lookAheadRange = 0
    i = 0
    while i < len(lst) - lookAheadRange:
        if lst[i+lookAheadRange] == item:
            lookAheadRange += 1
        else:
            lst[i] = lst[i+lookAheadRange]
            i += 1
    for _ in range(lookAheadRange):
        lst.pop()
    
if __name__ == "__main__":
    lst = [2,1,2,3,2,3,4,2,2]
    remove_all(lst, 2)
    print(lst)