import ctypes # provides low-level arrays
from typing import Iterable 
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iterable = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        if isinstance(iterable, Iterable):
            for i in iterable:
                self.append(i)


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (ind <= self.n - 1 or self.n - 1 + ind >= 0)):
            raise IndexError('invalid index')
        elif ind < 0:
            return self.data_arr[self.n - 1 + ind]
        else:
            return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (ind <= self.n - 1) or self.n - 1 + ind >= 0):
            raise IndexError('invalid index')
        elif ind < 0:
            self.data_arr[self.n - 1 + ind] = val
        else:
            self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self) -> str:
        return str(self.data_arr[:self.n])

    def __add__(self, other):
        new_array = ArrayList()
        for i in range(self.n):
            new_array.append(self[i])
        for i in range(other.n):
            new_array.append(other[i])
        return new_array

    def __iadd__(self, other):
        for i in range(other.n):
            self.append(other[i])
        return self

    def __mul__(self, multiplier):
        new_array = ArrayList()
        for i in range(self.n*multiplier):
            new_array.append(self[i % multiplier])
        return new_array

    def __rmul__(self, multiplier):
        return self.__mul__(multiplier)

    def remove(self, item):
        found_item = False
        i = 0
        while i < self.n:
            if self.data_arr[i] == item and not found_item:
                found_item = True
                self.n -= 1
            if found_item:
                if i != self.n:
                    self.data_arr[i] = self.data_arr[i+1]
            i += 1
    
    def removeAll(self, item):
        lookAheadRange = 0
        i = 0
        while i < self.n:
            if self.data_arr[i+lookAheadRange] == item:
                lookAheadRange += 1
                self.n -= 1
            else:
                self.data_arr[i] = self.data_arr[i+lookAheadRange]
                i += 1
    
    #part a
    def insert(self, index, val):
        if index < 0 or index > self.n:
            raise IndexError("Invalid index")
        elif index == self.n:
            self.append(val)
        else:
            if self.n == self.capacity:
                self.resize(self.capacity * 2)
            for i in range(self.n - 1, index - 1, -1):
                self.data_arr[i+1] = self.data_arr[i]
            self.data_arr[index] = val
            self.n += 1

    #part b and d
    def pop(self, index = None):
        if self.n == 0:
            raise IndexError("Pop called on empty list")
        else:
            if index != None:
                if index < 0 or index > self.n - 1:
                    raise IndexError("Invalid index")
                else:
                    popped_value = self.data_arr[index]
                    for i in range(index + 1, self.n):
                        self.data_arr[i - 1] = self.data_arr[i]
            else:
                popped_value = self.data_arr[self.n - 1]
            
            self.data_arr[self.n - 1] = None
            self.n -= 1
            if self.n < self.capacity // 4:
                self.resize(self.capacity // 2)
            return popped_value
    
if __name__ == "__main__":
    arr_lst = ArrayList()
    for i in range(1, 4+1):
        arr_lst.append(i)
    arr_lst.insert(2, 30)
    print(arr_lst)
    arr_lst = ArrayList()
    for i in range(1, 5+1):
        arr_lst.append(i)
    print(arr_lst.pop(3))
    print(arr_lst)
    while len(arr_lst) > 1:
        print(arr_lst.pop())
    print(arr_lst)
    print(arr_lst.capacity)
    arr_lst = ArrayList()
    for i in range(1, 5+1):
        arr_lst.append(i)
    print(arr_lst.pop(0))
    print(arr_lst.pop(1))