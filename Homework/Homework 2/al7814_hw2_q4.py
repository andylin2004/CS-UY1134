def e_approx(n):
    total = 0
    denominator = 1
    for i in range(n+1):
        if i != 0:
            denominator *= i
        total += 1 / denominator