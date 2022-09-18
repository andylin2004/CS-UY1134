def shift(lst, k):
    for _ in range(k):
        tmp = lst[0]
        for i in range(1, len(lst)):
            lst[i-1] = lst[i]
        lst[len(lst)-1] = tmp