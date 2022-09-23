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
#part a

def move_zeros(nums): 
    """
    : nums type: list[int]
    : return type: None
    """

    zeroToMove = -1
    i = 0
    while i < len(nums):
        print(i)
        if nums[i] != 0 and zeroToMove != -1 and zeroToMove < i:
                nums[zeroToMove] = nums[i]
                nums[i] = 0
                tmp = zeroToMove
                zeroToMove = i
                i = tmp
        elif zeroToMove > i and nums[i] == 0:
            zeroToMove = i
            i-=1
        i += 1

list = [0, 1, 0, 3, 13, 0]
move_zeros(list)
print(list)