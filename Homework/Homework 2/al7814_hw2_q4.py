def e_approx(n):
    total = 0
    denominator = 1
    for i in range(n+1):
        if i != 0:
            denominator *= i
        total += 1 / denominator
    return total

if __name__ == "__main__":
    def main():
        for n in range(15):
            curr_approx = e_approx(n)
            approx_str = "{:.15f}".format(curr_approx)
            print("n =", n, "Approximation:", approx_str)
    
    main()