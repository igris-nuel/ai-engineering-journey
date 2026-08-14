from dot import Vector

class Matrix:
    def __init__(self, rows):
        if not rows:
            raise ValueError("Matrix cannot be empty")
        
        self._rows = [list(row) for row in rows]

        column_count = len(self._rows[0])

        if column_count == 0:
            raise ValueError("Matrix cannot have empty rows")


        if any(len(row) != column_count for row in self._rows):
            raise ValueError("All rows must have the same length.")

    @property
    def shape(self):
        return(len(self._rows), len(self._rows[0]))

    def __repr__(self):
        return f"Matrix{self._rows}"

    def __matmul__(self, vector):
        if not isinstance(vector, Vector):
            return NotImplemented

        rows, columns = self.shape

        if columns !=  vector.dimension:
             raise ValueError(
            "Matrix columns must match "
            "vector dimension."
        )

        return Vector([sum(x*y for x,y in zip(row, vector)) for row in self._rows])

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, column = index
            return self._rows[row][column]
        return self._rows[index]

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, column = index
            self._rows[row][column] = value
        else:
            self._rows[index] = list(value)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.shape != other.shape:
            raise ValueError("matrice must have the same shape")
        
        return Matrix([u+v for u,v in zip(x, y)] for x, y in zip(self, other)
            )

    def __mul__(self, scalar):
        if not isinstance(scalar, (float, int)):
            return NotImplemented

        return Matrix([x * scalar for x in y] for y in self)
    __rmul__ = __mul__

    def transpose(self):
        return Matrix([list(row) for row in zip(*self._rows)])

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        
        Other_row, Other_column = other.shape
        self_row, self_column = self.shape

        if self_row != Other_column:
            raise ValueError("Matrices are completely incompatible for multiplication.")

        



    
A = Matrix([[1, 2], [4, 6]])

# print(A)
# print(A.shape)
A = Matrix([
    [1, 3],
    [2, 4]
])

B = Matrix([
    [1, 3],
    [2, 4]
])


x = Vector([2, 3])

print(A) 
print(A.transpose()) 
# print(A + B) 
