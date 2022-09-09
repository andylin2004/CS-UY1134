from random import randint

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

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __repr__(self):
        if self.b < 0:
            return str(self.a) + " - " + str(self.b * -1) + "i"
        return str(self.a) + " + " + str(self.b) + "i"

    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b


#TEST CODE
'''
def __add__(self, other):
cplx1 + cplx2
In this example, self refers to cplx1 since it is the first argument and other would refer to cplx2 since it is the second argument.
'''
#constructor, output
cplx1 = Complex(5, 2)
print(cplx1) #5 + 2i
cplx2 = Complex(3, 3)
print(cplx2) #3 + 3i
#addition
print(cplx1 + cplx2) #8 + 5i
#subtraction
print(cplx1 - cplx2) #2 - 1i
# multiplication First Outer Inner Last cplx1 * cplx2 (5 + 2i)(3 + 3i) -> multiply (5*3) + (5*3i) + (2i*3) + (2i*3i) = 15 + 15i + 6i + 6(i^2) -> simplify = 15 + 21i + 6(-1) = 9 + 21i
print(cplx1 * cplx2) #9 + 21i
# original objects remain unchanged
print(cplx1) #5 + 2i
print(cplx2) #3 + 3i

# question 3a
def create_permutation(n):
    intRange = []
    for i in range(n):
        if len(intRange) == 0:
            intRange.append(i)
        elif len(intRange) == 1:
            if randint(0,1):
                intRange.append(i)
            else:
                intRange.insert(0, len(intRange))
        else:
            intRange.insert(randint(0, len(intRange)), i)

    return intRange

for _ in range(2):
    print(create_permutation(6))

# question 3b
def scramble_word(word):
    scrambled_positions = create_permutation(len(word))
    
    new_word = ""
    
    for i in scrambled_positions:
        new_word += word[i]

    return new_word

for i in range(2):
    print(scramble_word("pokemon"))

# question 3c

def scramble_word_game(word):
    scrambled_word = scramble_word(word)
    outString = "Unscramble the word:"
    for char in scrambled_word:
        outString += "  " + char
    print(outString)
    for i in range(3):
        inputString = input("Try #"+str(i)+": ")
        if inputString == word:
            print("Yay, you got it!")
            return
        else:
            print("Wrong!")
    
    print("Too bad! You lose!")

scramble_word_game("amogus")