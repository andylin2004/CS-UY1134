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

# part b
def reverse_list(lst, low = None, high = None):
    """
    : lst type: list[]
    : low, high type: int
    : return type: None
    """
    if low == high == None:
        low = 0
        high = len(lst) - 1
    
    for i in range(low, ((high + 1 - low) // 2) + low):
        tmp = lst[i]
        lst[i] = lst[high+1-i]
        lst[high+1-i] = tmp

list = [1,2,3,4,5,6]
reverse_list(list, 1, 3)
print(list)

#question 2

def move_zeros(nums): 
    """
    : nums type: list[int]
    : return type: None
    """

    move_zero_at = 0
    for i in range(len(nums)):
        if nums[i] == 0 and (i < move_zero_at or (nums[move_zero_at] != 0 and move_zero_at == 0)):
            move_zero_at = i
        elif i > move_zero_at and nums[i] != 0:
            nums[i], nums[move_zero_at] = nums[move_zero_at], nums[i]
            move_zero_at += 1

list = [0, 1, 0, 3, 13, 0]
move_zeros(list)
print(list)

#question 3

def shift(lst, k, shift_direction = "left"):
    if shift_direction == "left":
        for _ in range(k):
            tmp = lst[0]
            for i in range(1, len(lst)):
                lst[i-1] = lst[i]
            lst[len(lst)-1] = tmp
    elif shift_direction == "right":
        for _ in range(k):
            tmp = lst[len(lst) - 1]
            for i in range(len(lst) - 2, -1, -1):
                lst[i+1] = lst[i]
            lst[0] = tmp

list = [1,2,3,4,5,6]
shift(list, 2)
print(list)

list = [1,2,3,4,5,6]
shift(list, 2, 'right')
print(list)
