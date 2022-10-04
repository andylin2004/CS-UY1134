def two_sum(srt_lst, target):
    for i in range(len(srt_lst)):
        compliment = target - srt_lst[i]
        left = 0
        right = len(srt_lst) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if srt_lst[mid] > compliment:
                right = mid
            elif srt_lst[mid] < compliment:
                left = mid
            elif srt_lst[mid] == compliment:
                return (i, mid)
        if srt_lst[left] == compliment:
            return (i, left)
        elif srt_lst[right] == compliment:
            return (i, right)
    return None

if __name__ == "__main__":
    print(two_sum([-2, 7, 11, 15, 20, 21,22], 33))