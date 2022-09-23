# question 1
# part a
def reverse_list(lst):
    """
    : lst type: list[] 
    : return type: None
    """
    for i in range(len(lst)//2):
        tmp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = tmp

list = [1,2,3,4,5,6]
reverse_list(list)
print(list)