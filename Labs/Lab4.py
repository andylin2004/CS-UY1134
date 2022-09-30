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