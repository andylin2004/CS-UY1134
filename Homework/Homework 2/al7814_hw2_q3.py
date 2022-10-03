from math import sqrt

def factors(num):
    for i in range(1, round(sqrt(num)) + 1):
        if num % i == 0:
            yield i

for curr_factor in factors(100):
    print(curr_factor)
