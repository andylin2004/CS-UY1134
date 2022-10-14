#q1
def sum_to(n):
    if n <= 1:
        return 1
    else:
        return n + sum_to(n-1)

print(sum_to(16))
print(sum([x for x in range(17)]))

#q2
def product_evens(n):
    if n <= 2:
        return 2
    else:
        return n * product_evens(n-2)

print(product_evens(8))