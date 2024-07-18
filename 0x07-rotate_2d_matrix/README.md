# Matrix Rotation 90 Degrees Clockwise

This project aims to rotate an `n x n` 2D matrix 90 degrees clockwise in-place using Python.

## Approach

The rotation of a matrix can be efficiently achieved in two main steps:

1. **Transpose the Matrix**:
   - Transpose the matrix by swapping elements across its diagonal. This step converts rows into columns.

2. **Reverse Each Row**:
   - After transposing, reverse each row of the matrix. This action ensures that the columns are effectively rotated to the right.

## Implementation Steps

### Step-by-Step Implementation:

1. **Transpose the Matrix**:
   - Iterate through the matrix and swap `matrix[i][j]` with `matrix[j][i]` for all valid indices `i` and `j`.

2. **Reverse Each Row**:
   - After transposing, iterate through each row of the matrix and reverse its elements.

3. **In-Place Modification**:
   - Ensure that all operations are performed directly on the original matrix without creating a new matrix.

### Example

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

### Usage

- Replace `matrix` with your desired input matrix.
- Call `rotate_2d_matrix(matrix)` to rotate the matrix in-place.
- Print or use `matrix` as needed after rotation.

### Requirements

- Python 3.x environment.
- Ensure all Python files start with `#!/usr/bin/python3` and end with a newline.
- Follow PEP 8 guidelines for code style (`pycodestyle`).

### Notes

- This implementation assumes the matrix is square (`n x n`) and non-empty.
- Edge cases, such as single-row matrices, are naturally handled by the function.
