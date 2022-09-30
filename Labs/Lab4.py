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