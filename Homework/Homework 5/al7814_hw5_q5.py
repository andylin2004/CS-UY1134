from ArrayStack import *
from ArrayQueue import *
from copy import copy

def permutations(lst):
    if len(lst) == 0:
        return []
    permutations = ArrayQueue()
    numbers_to_use = ArrayStack()
    for i in lst:
        permutations.enqueue([i])
    while len(permutations.first()) != len(lst):
        for i in range(len(permutations)):
            for v in lst:
                numbers_to_use.push(v)
            while not numbers_to_use.is_empty():
                candidate_number = numbers_to_use.pop()
                to_add_into_permutations = copy(permutations.first())
                if candidate_number not in to_add_into_permutations:
                    to_add_into_permutations.append(candidate_number)
                    permutations.enqueue(to_add_into_permutations)
            permutations.dequeue()
    result = []
    while not permutations.is_empty():
        result.append(permutations.dequeue())
    return result

if __name__ == "__main__": 
    print(len(permutations([1,2,3,4,5,6])))