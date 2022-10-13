def removeAll(lst, item):
    lookAheadRange = 0
    i = 0
    while i < len(lst):
        if lst[i+lookAheadRange] == item:
            lookAheadRange += 1
        else:
            lst[i] = lst[i+lookAheadRange]
            i += 1