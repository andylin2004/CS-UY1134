def appearances(s, low, high):
    dictionary = {}
    if low != high:
        dictionary = appearances(s, low+1, high)
    if s[low] in dictionary:
        dictionary[s[low]] += 1
    else:
        dictionary[s[low]] = 1
    return dictionary

if __name__ == "__main__": 
    string = "Hello World"
    print(appearances(string, 0, 10))