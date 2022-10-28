#part a

def count_lowercase(s, low, high):
    total = 0
    if low != high:
        total += count_lowercase(s, low+1, high)
    if 97 <= ord(s[low]) < 123:
        total += 1
    return total

#part b

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return True
    else:
        if 97 <= ord(s[low]) < 123:
            return not is_number_of_lowercase_even(s, low+1, high)
        else:
            return is_number_of_lowercase_even(s, low+1, high)

if __name__ == "__main__": 
    string = "kanYE"
    print(count_lowercase(string, 0, len(string) - 1))
    print(is_number_of_lowercase_even(string, 0, len(string) - 1))