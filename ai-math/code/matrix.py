from dot import Vector

class Matrix:
    def __init__(self, rows):
        if not rows:
            raise ValueError("Matrix cannot be empty")
        
        self._rows = [list(row) for row in rows]

        column_count = len(self._rows)

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

        result = []

        for row in self._rows:
            value = sum(x*y for x,y in zip(row, vector))

            result.append(value)

        return Vector(result)
        

    
A = Matrix([[1, 2], [4, 6]])

print(A)
print(A.shape)
A = Matrix([
    [1, 3],
    [2, 4]
])

x = Vector([2, 3])

print(A @ x)
