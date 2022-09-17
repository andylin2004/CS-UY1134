#part a

def sum_under_square(n):
    total = 0
    base = 1
    while base ** 2 < n:
        total += base ** 2
        base += 1
    
    return total

if __name__ == "__main__":
    print(sum_under_square(17))