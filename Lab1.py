# question 1

def can_construct(word , letters): 
    """
    word - type: str
    letters - type: str
    return value - type: bool
    """

    possibleLetters = []

    for char in letters:
        possibleLetters.append(char)

    for char in word:
        if char in possibleLetters:
            possibleLetters.remove(char)
        else:
            return False
    
    return True

print(can_construct("apples", "aples"))
print(can_construct("apples", "aplespl"))

