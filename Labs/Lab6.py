#q1
from asyncio import constants


def sum_to(n):
    if n <= 1:
        return 1
    else:
        return n + sum_to(n-1)

print(sum_to(16))
print(sum([x for x in range(17)]))

#q2
def product_evens(n):
    if n <= 2:
        return 2
    else:
        return n * product_evens(n-2)

print(product_evens(8))

#q3
def find_max(lst, low, high):
    if high - low == 0:
        return lst[0]
    elif high - low == 1:
        if lst[low] > lst[high]:
            return lst[low]
        else:
            return lst[high]
    prev = find_max(lst, low + 1, high - 1)
    if prev > lst[low] and prev > lst[high]:
        return prev
    elif lst[low] > lst[high] and lst[low] > prev:
        return lst[low]
    else:
        return lst[high]

print(find_max([13,9,17,29,3,4,2], 0, 5))

#q4
def is_palindrome(str, low, high):
    if high - low <= 0:
        return True
    else:
        return str[low] == str[high] and is_palindrome(str, low + 1, high - 1)

print(is_palindrome("555", 0, 2))

#q5
def binary_search(lst, low, high, val):
    mid = (low + high) // 2
    if high - low <= 1:
        if lst[high] == val:
            return high
        elif lst[low] == val:
            return low
        else:
            return None
    elif lst[mid] > val:
        return binary_search(lst, low, mid, val)
    elif lst[mid] == val:
        return mid
    else:
        return binary_search(lst, mid + 1, high, val)

print(binary_search([1,12,15,18,420], 0, 4, 18))

#q6
def vc_count(word, low, high):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowelCount = 0
    consonantsCount = 0
    if high - low <= 1:
        if high - low == 1:
            if word[low] in vowels:
                vowelCount += 1
            else:
                consonantsCount += 1
        if word[high] in vowels:
            vowelCount += 1
        else:
            consonantsCount += 1
        return (vowelCount, consonantsCount)
    else:
        previous = vc_count(word, low + 1, high - 1)
        vowelCount = previous[0]
        consonantsCount = previous[1]
        if word[low] in vowels:
            vowelCount += 1
        else:
            consonantsCount += 1
        if word[high] in vowels:
            vowelCount += 1
        else:
            consonantsCount += 1
        return (vowelCount, consonantsCount)

word = "NYUTandonEngineering"
print(vc_count(word, 0, len(word)-1))