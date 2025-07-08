# MATRIX-TOOL
A Python-based Matrix Operations Tool using NumPy with a simple CLI. It supports addition, subtraction, multiplication, transpose, inverse, determinant, rank, and checks for symmetry and identity. Designed for students and beginners to practice linear algebra and matrix computations in an interactive, modular way.

## 📊 Project Overview

**Project Title**: Matrix Operations Tool using NumPy
**Level**: Beginner
**Technology**: Python, NumPy

This project is built to demonstrate basic matrix operations using Python and the NumPy library. It features a menu-driven command-line interface where users can perform various matrix computations such as addition, subtraction, multiplication, transpose, inverse, determinant, and more. The project is ideal for beginners who are learning linear algebra or starting with NumPy, and it provides a solid foundation for understanding matrix manipulation in a practical, interactive format.

## 🎯 Objectives

**1. Create a CLI-based tool**: Develop a command-line interface for interactive matrix operations.

**2. Implement core operations**: Enable users to perform addition, subtraction, multiplication, transpose, determinant, inverse, and rank calculations.

**3. Use NumPy efficiently**: Apply NumPy’s built-in functions to handle matrix computations accurately and efficiently.

**4. Introduce matrix properties**: Include checks for symmetry, identity, and square matrices to enhance conceptual understanding.

## 🧱 Project Structure

*1. Matrix Creation*

***Functionality***: Accepts user input to create a matrix with specified rows and columns.

***Implementation***: Uses NumPy's array and reshape methods to convert user input into a matrix format

```python
def matrix_creation():
    rows = int(input("\nenter rows count:"))
    columns = int(input("\nenter columns count:"))
    print("enter matrix elements(space)")
    elements = list(map(float, input().split()))
    return np.array(elements).reshape(rows, columns)
```

*2. Matrix Addition*

***Functionality***: Adds two matrices element-wise.

***Requirement***: Both matrices must have the same dimensions.

***Implementation***: Utilizes the + operator directly on NumPy arrays.

```python
# Matrix addition
def addition(a, b):
    return a + b
```

*3. Matrix Multiplication*

***Functionality***: Performs matrix multiplication (dot product).

***Requirement***: Number of columns in the first matrix must equal the number of rows in the second.

***Implementation***: Uses np.dot() for multiplication.

```python
# Matrix multiplication (dot product)
def multiplication(a, b):
    return np.dot(a, b)
```

*4. Matrix Subtraction*

***Functionality***: Subtracts the second matrix from the first, element-wise.

***Requirement***: Both matrices must have the same dimensions.

***Implementation***: Uses the - operator on NumPy arrays.

```python
# Matrix subtraction
def subtraction(a, b):
    return a - b
```

*5. Matrix Transpose*

***Functionality***: Converts rows into columns and vice versa.

***Implementation***: Uses NumPy’s .T attribute to transpose the matrix.

```python
# Transpose of a matrix
def transpose(a):
    return a.T
```

*6. Scalar Multiplication*

***Functionality**: Multiplies every element of a matrix by a scalar value.

***Implementation***: Multiplies the scalar with the NumPy array directly.

```python
# Scalar multiplication
def scalar_multiplication(scalar, A):
    return scalar * A
```

*7. Determinant Calculation*

***Functionality***: Computes the determinant of a square matrix.

***Requirement***: Matrix must be square (rows = columns).

***Implementation***: Uses np.linalg.det() from NumPy’s linear algebra module.

```python
# Determinant of a square matrix
def determinant(A):
    return np.linalg.det(A)
```

*8. Inverse of a Matrix*

***Functionality***: Calculates the inverse of a square matrix.

***Requirement***: Matrix must be square and non-singular (determinant ≠ 0).

***Implementation***: Uses np.linalg.inv().

```python
# Inverse of a square matrix
def inverse(A):
    return np.linalg.inv(A)
```

*9. Matrix Rank*

***Functionality***: Finds the rank of a matrix (maximum number of linearly independent row/column vectors).

***Implementation***: Uses np.linalg.matrix_rank().

```python
# Rank of a matrix
def rank(A):
    return np.linalg.matrix_rank(A)
```

*10. Matrix Property Checks*

***Symmetric Check***: Verifies if a matrix is equal to its transpose.

***Identity Check***: Verifies if a matrix is a square identity matrix using np.eye().

```python
# Check if matrix is identity (square and equal to np.eye)
def is_identity(A):
    return np.array_equal(A, np.eye(A.shape[0])) if check_square(A) else False
```
*11. check square*

```python
# Check if matrix is square (rows == columns)
def check_square(A):
    return A.shape[0] == A.shape[1]
```

