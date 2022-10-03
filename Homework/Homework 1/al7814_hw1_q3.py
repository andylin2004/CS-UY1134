#part a

def sum_under_square(n):
    total = 0
    base = 1
    while base < n:
        total += base ** 2
        base += 1
    
    return total

# part b

def iter_sum_under_square(n):
    return sum([x ** 2 for x in range(n)])

# part c

def sum_under_odd_square(n):
    total = 0
    base = 1
    while base ** 2 < n:
        total += base ** 2
        base += 2
    
    return total

# part d

def gen_next_odd_square(n):
    base = 1
    while base ** 2 < n:
        yield base ** 2
        base += 2

def iter_sum_under_odd_square(n):
    return sum([x for x in gen_next_odd_square(n)])

if __name__ == "__main__":
    print(sum_under_square(17))
    print(iter_sum_under_square(17))
    print(sum_under_odd_square(17))
    print(iter_sum_under_odd_square(17))