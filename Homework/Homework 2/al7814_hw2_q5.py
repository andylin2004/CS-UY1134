def split_parity(lst):
    left = 0
    right = len(lst) - 1
    while right > left:
        if lst[left] % 2 == 0 and lst[right] % 2 == 1:
            (lst[right], lst[left]) = (lst[left], lst[right])
        if lst[left] % 2 == 1:
            left += 1
        if lst[right] % 2 == 0:
            right -= 1

if __name__ == "__main__":
    lst = [1,2,3,4]
    split_parity(lst)
    print(lst)