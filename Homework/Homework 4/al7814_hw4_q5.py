#part a

def count_lowercase(s, low, high):
    total = 0
    if 97 <= ord(s[low]) < 123:
        total += 1
    if low != high:
        total += count_lowercase(s, low+1, high)
    return total

if __name__ == "__main__": 
    string = "kanYe"
    print(count_lowercase(string, 0, len(string) - 1))