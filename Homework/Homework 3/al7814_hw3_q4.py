def removeAll(lst, item):
    lookAheadRange = 0
    i = 0
    while i < len(lst) - lookAheadRange:
        if lst[i+lookAheadRange] == item:
            lookAheadRange += 1
        else:
            lst[i] = lst[i+lookAheadRange]
            i += 1
    
if __name__ == "__main__":
    lst = [2,1,2,3,2,3,4,2,2]
    removeAll(lst, 2)
    print(lst)