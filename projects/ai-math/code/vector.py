
# Vector space

import numpy as np


u = np.array([2, 3])
v = np.array([3, 5])

# Vector addition
print(u+v)

#Vector multiplication
print(2 * v)




# pythonic way

class Vector:
    def __init__(self, values:list[float]):
        if not values:
            raise ValueError(
                "Vector cannot be empty."
            )

        self._values = list(values)

    @property
    def value(self):
        return tuple(self._values)

    def to_list(self):
        return self._values.copy()

    @property
    def is_empty(self):
        return len(self._values) == 0
    
    @property
    def dimension(self):
        return len(self._values)

    def copy(self):
        return Vector(self._values.copy())

    def __repr__(self):
        return f"Vector({self._values})"

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __contains__(self, value):
        return value in self._values
            
    def __iter__(self):
        return iter(self._values)

    def __eq__(self, item):
        if not isinstance(item, Vector):
            return NotImplemented
        return item._values == self._values

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise ValueError("Mismatch vectors")

        return Vector([x+y for x, y in zip(self, other)])

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        
        return Vector([scalar * value for value in self._values])

    __rmul__ = __mul__

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise ValueError("vectors not matched")
        
        return Vector([x-y for x, y in zip(self, other)])

    def __truediv__(self, scalar:float):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide a vector by zero.")
        return Vector([value / scalar  for value in self._values])     

    def __neg__(self):
        return Vector([-x for x in self._values])

    

user = Vector([2, 5, 4, 10])

print(user)
print(user.dimension)

print(user[3])

print(34 in user)


for x in user:
    print(x)

print(user.copy())

print(user.copy() == user)

print(user.is_empty)


u = Vector([2,4,6,7])
v = Vector([4, 6, 7, 8])

print(u+v)
print(5 * u)