def print_triangle(n):
    print_triangle_recursive(1, n)

def print_triangle_recursive(cur, max):
    print("*" * cur)
    if cur < max:
        print_triangle_recursive(cur + 1, max)


if __name__ == "__main__": 
    print_triangle(4)