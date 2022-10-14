#q1
def sum_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_to(n-1)

print(sum_to(16))
print(sum([x for x in range(17)]))