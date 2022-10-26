#part a

def print_triangle(n):
    if n > 1:
        print_triangle(n - 1)
    print("*" * n)

#part b

def print_opposite_triangles(n):
    print("*" * n)
    if n > 1:
        print_opposite_triangles(n - 1)
    print("*" * n)

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
    print_opposite_triangles(4)
    print()
    print_ruler(5)