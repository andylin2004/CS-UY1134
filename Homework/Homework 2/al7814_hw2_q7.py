def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    while True:
        mid = (left + right) // 2
        if right - left == 1:
            if lst01[left] == 1:
                return left
            if lst01[right] == 1:
                return right
            else:
                return None
        if lst01[left] == lst01[mid] == 0:
            left = mid + 1
        elif lst01[mid] == 1:
            right = mid
        else:
            return None

if __name__ == "__main__":
    print(findChange([0, 0, 0, 1, 1, 1, 1, 1]))