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

# question 2

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)