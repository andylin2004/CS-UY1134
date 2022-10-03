# question 1
'''PATTERN: TWO POINTERS MOVING INWARD -> <-'''
def is_palindrome(s): 
    """
    : s type: str
    : return type: bool
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1-i]:
            return False

    return True

print(is_palindrome("55055"))

# question 2

def is_vovel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

def reverse_vowels(input_str):
    """
    : input_str type: string
    : return type: string
    """
    list_str = list(input_str) #list constructor guarantees Theta(n)
    # Your code implementation goes here
    left = 0
    right = len(list_str)-1
    while (left < len(list_str) or right >= 0) and left < right:
        if not is_vovel(list_str[left]):
            left += 1
        if not is_vovel(list_str[right]):
            right -= 1
        if is_vovel(list_str[left]) and is_vovel(list_str[right]):
            (list_str[left], list_str[right]) = (list_str[right], list_str[left])
            left += 1
            right -= 1
    return "".join(list_str)

print(reverse_vowels("agar.io"))

# question 3
# part b

def find_missing(lst):
    """
    : nums type: list[int] (sorted)
    : return type: int
    """
    left = 0
    right = len(lst) - 1
    while True:
        mid = (left + right) // 2 
        if right - left == 1:
            if lst[left] != left:
                return left
            elif lst[right] != right:
                return right
            else:
                return None
        elif lst[mid] != mid and lst[right] != right:
            right = mid
        elif lst[right] != right:
            left = mid
        else:
            return None

print(find_missing([0,1,2,3,4,5,7,8,9]))

# part c

def find_missing_unsorted(lst):
    """
    : nums type: list[int] (unsorted)
    : return type: int
    """
    lst_total = sum(lst)
    return len(lst)*(len(lst) + 1)//2 - lst_total

print(find_missing_unsorted([8, 6, 0, 4, 3, 5, 1, 2]))

# question 4
# part 1

def find_pivot(lst):
    """
    : lst type: list[int] #sorted and then shifted
    : val type: int
    : return type: int (index if found), None(if not found)
    """
    left = 0
    right = len(lst) - 1
    while True:
        mid = (left + right) // 2
        if right-left == 1:
            if lst[left] < lst[right]:
                return left
            else:
                return right
        if lst[left] > lst[mid]:
            right = mid
        elif lst[mid] > lst[right]:
            left = mid

print(find_pivot([3, 6, 7, 10, 12, 14,15,20,21, 1,]))