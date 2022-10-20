#part a

def print_triangle(n):
    print_triangle_recursive(1, n)

def print_triangle_recursive(cur, max):
    print("*" * cur)
    if cur < max:
        print_triangle_recursive(cur + 1, max)


#part b

def print_decreasing_triangle_recursive(n):
    print("*" * n)
    if n > 1:
        print_decreasing_triangle_recursive(n - 1)

def print_opposite_triangle(n):
    print_decreasing_triangle_recursive(n)
    print_triangle(n)

#part c

def print_ruler(n):
    if n > 1:
        print_ruler(n-1)
    print("-" * n)
    if n > 1:
        print_ruler(n-1)

if __name__ == "__main__": 
    print_triangle(4)
    print()
    print_opposite_triangle(4)
    print()
    print_ruler(5)