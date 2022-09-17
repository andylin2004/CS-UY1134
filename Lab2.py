# question 1

class Polynomial:
    def __init__(self, coefficients):
        self.data = coefficients

    def __add__(self, other):
        coefficents = []
        for i in range(max(len(self.data), len(other.data))):
            coefficents.append(0)
            if i < len(self.data):
                coefficents[i] += self.data[i]
            if i < len(other.data):
                coefficents[i] += other.data[i]

        return Polynomial(coefficents)
    def __call__(self, param):
        total = 0
        for i in range(len(self.data)):
            total += self.data[i] * (param ** i)
        
        return total

poly1 = Polynomial([3, 7, 0, -9, 2]); # represents 2x4 - 9x3 + 7x + 3 
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]); # represents 3x6 + 5x3 + 2
poly3 = poly1 + poly2
print(poly3.data) # return [5, 7, 0, -4, 2, 0, 3]
print(poly1(1)) # return 3
print(poly2(1)) # return 10
print(poly3(1)) # return 13

# question 2

def powers_of_two(n):
    for i in range(n):
        yield 2 ** i

for i in powers_of_two(6):
    print(i)

# question 3

class UnsignedBinaryInteger:
    def __init__(self, num_str):
        self.num_str = num_str
    
    def __eq__(self, other):
        return self.num_str == other.num_str

    def __lt__(self, other):
        if self.num_str == other.num_str:
            return False
        elif len(self.num_str) == len(other.num_str):
            for i in range(len(self.num_str)):
                if int(self.num_str[i]) != int(other.num_str[i]):
                    return int(self.num_str[i]) < int(other.num_str[i])
        else:
            return len(self.num_str) < len(other.num_str)

    def __gt__(self, other):
        if self.num_str == other.num_str:
            return False
        elif len(self.num_str) == len(other.num_str):
            for i in range(len(self.num_str)):
                if int(self.num_str[i]) != int(other.num_str[i]):
                    return int(self.num_str[i]) > int(other.num_str[i])
        else:
            return len(self.num_str) > len(other.num_str)

    def is_twos_power(self):
        onesCount = 0
        for digit in self.num_str:
            if digit == '1':
                onesCount += 1
                if onesCount > 1:
                    return False
        return True

    def largest_twos_power(self):
        largestPowerToUse = -1
        for i in range(len(self.num_str)):
            if self.num_str[len(self.num_str) - 1 - i] == '1':
                largestPowerToUse = i
        
        if largestPowerToUse != -1:
            return 2 ** largestPowerToUse
        
        return 0

    def __repr__(self):
        return "0b"+self.num_str

num = UnsignedBinaryInteger("1101")
print(num.is_twos_power())
print(num.largest_twos_power())
num2 = UnsignedBinaryInteger("1111")
print(num2.is_twos_power())
print(num2.largest_twos_power())
num3 = UnsignedBinaryInteger("1000")
print(num3.is_twos_power())
print(num3.largest_twos_power())
print(num > num2)
print(num < num2)
print(num > num3)
print(num < num3)
print(num2 > num3)
print(num2 < num3)