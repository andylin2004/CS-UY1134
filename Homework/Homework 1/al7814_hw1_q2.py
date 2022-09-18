def shift(lst, k, shift_direction = "left"):
    if shift_direction == "left":
        for _ in range(k):
            tmp = lst[0]
            for i in range(1, len(lst)):
                lst[i-1] = lst[i]
            lst[len(lst)-1] = tmp
    elif shift_direction == "right":
        for _ in range(k):
            tmp = lst[len(lst) - 1]
            for i in range(len(lst) - 2, -1, -1):
                lst[i+1] = lst[i]
            lst[0] = tmp

if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    print(lst)
    shift(lst, 2)
    print(lst)
    shift(lst, 2, "right")
    print(lst)