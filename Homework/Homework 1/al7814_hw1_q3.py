#part a

def sum_under_square(n):
    total = 0
    base = 1
    while base ** 2 < n:
        total += base ** 2
        base += 1
    
    return total

# part b

def gen_next_square(n):
    base = 1
    while base ** 2 < n:
        yield base ** 2
        base += 1

if __name__ == "__main__":
    print(sum_under_square(17))
    print(sum([x for x in gen_next_square(17)]))