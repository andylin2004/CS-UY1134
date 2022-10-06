from random import randint

def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if lst01[left] == lst01[mid] == 0:
            left = mid + 1
        elif lst01[mid] == 1:
            right = mid
        else:
            return None
    if right - left == 1:
        if lst01[left] == 1:
            return left
        elif lst01[right] == 1:
            return right
        else:
            return None
    elif right - left == 0:
        if lst01[0] == 1:
            return 0

if __name__ == "__main__":
    lst = []
    zero = True
    for i in range(1000000000000):
        if randint(0,100) == 1:
            zero = False
        if zero:
            lst.append(0)
        else:
            lst.append(1)
    print(lst)
    print(findChange(lst))
    print(findChange([0,1]))