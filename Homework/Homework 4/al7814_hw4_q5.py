#part a

def count_lowercase(s, low, high):
    total = 0
    if 97 <= ord(s[low]) < 123:
        total += 1
    if low != high:
        total += count_lowercase(s, low+1, high)
    return total

#part b

def is_number_of_lowercase_even(s, low, high):
    return count_lowercase(s, low, high) % 2 == 0

if __name__ == "__main__": 
    string = "kanYE"
    print(count_lowercase(string, 0, len(string) - 1))
    print(is_number_of_lowercase_even(string, 0, len(string) - 1))