import math

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

    # def distance(self, other):
    #     if not isinstance(other, Vector):
    #         raise TypeError(
    #             "Distance requires another Vector."
    #         )
    #     if self.dimension != other.dimension:
    #         raise ValueError("vectors not matched")
    #     distance = sum((x -y)**2 for x, y in zip(self, other))

    #     return math.sqrt(distance)

    def norm(self)->float:
        return math.sqrt(
            sum(x**2 for x in self)
        )

    def distance(self, other):
        if not isinstance(other, Vector):
              raise TypeError(
                "Distance requires another Vector."
             )
        if self.dimension != other.dimension:
            raise ValueError("vectors not matched")
        return (self-other).norm()

    def dot(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise ValueError("vectors dimensions not equal")

        return sum(
            (x*y for x, y in zip(self, other))
        )

    def cosine_similarity(self, other) -> float:
        if not isinstance(other, Vector):
            raise TypeError("Cosine similarity requires another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension.")
            
        v_norm = self.norm()
        u_norm = other.norm()
        
        if v_norm == 0 or u_norm == 0:
            raise ValueError("Cannot calculate similarity with a zero vector.")
            
        similarity = self.dot(other) / (v_norm * u_norm)
        
        return max(-1.0, min(1.0, similarity))



    def angle(self,other):
        result = self.cosine_similarity(other)

        return math.degrees(math.acos(result))
    


u = Vector([1, 2, 2])
v = Vector([4, 0, 3])
print(u.distance(v))
print(u.cosine_similarity(v))



# import numpy as np

# u = np.array([2,3])
# v = np.array([5,7])

# distance = np.linalg.norm(u-v)

# print(distance)

