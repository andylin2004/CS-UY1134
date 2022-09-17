class Vector:
    def __init__(self, d):
        if isinstance(d) == int:
            self.coords = [0]*d
        elif isinstance(d) == list:
            self.coords = list

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)
    
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result
    
    def __neg__(self):
        result = Vector(self.coords)
        for i in range(len(result)):
            result[i] *= -1
        return result

    def __mul__(self, multiplier):
        result = Vector(self.coords)
        for i in range(result):
            result[i] *= multiplier
        return result

    def __rmul__(self, multiplier):
        result = Vector(self.coords)
        for i in range(result):
            result[i] *= multiplier
        return result