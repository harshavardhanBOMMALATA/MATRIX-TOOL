# MATRIX-TOOL
A Python-based Matrix Operations Tool using NumPy with a simple CLI. It supports addition, subtraction, multiplication, transpose, inverse, determinant, rank, and checks for symmetry and identity. Designed for students and beginners to practice linear algebra and matrix computations in an interactive, modular way.

## 📊 Project Overview

**Project Title**: Matrix Operations Tool using NumPy
**Level**: Beginner
**Technology**: Python, NumPy

This project is built to demonstrate basic matrix operations using Python and the NumPy library. It features a menu-driven command-line interface where users can perform various matrix computations such as addition, subtraction, multiplication, transpose, inverse, determinant, and more. The project is ideal for beginners who are learning linear algebra or starting with NumPy, and it provides a solid foundation for understanding matrix manipulation in a practical, interactive format.

## 🎯 Objectives

* **Create a CLI-based tool**: Develop a command-line interface for interactive matrix operations.

* **Implement core operations**: Enable users to perform addition, subtraction, multiplication, transpose, determinant, inverse, and rank calculations.

* **Use NumPy efficiently**: Apply NumPy’s built-in functions to handle matrix computations accurately and efficiently.

* **Introduce matrix properties**: Include checks for symmetry, identity, and square matrices to enhance conceptual understanding.

## 🧱 Project Structure

*1. Matrix Creation*

* ***Functionality***: Accepts user input to create a matrix with specified rows and columns.

* ***Implementation***: Uses NumPy's array and reshape methods to convert user input into a matrix format

```python
def matrix_creation():
    rows = int(input("\nenter rows count:"))
    columns = int(input("\nenter columns count:"))
    print("enter matrix elements(space)")
    elements = list(map(float, input().split()))
    return np.array(elements).reshape(rows, columns)
```

*2. Matrix Addition*

* ***Functionality***: Adds two matrices element-wise.

* ***Requirement***: Both matrices must have the same dimensions.

* ***Implementation***: Utilizes the + operator directly on NumPy arrays.

```python
# Matrix addition
def addition(a, b):
    return a + b
```

*3. Matrix Multiplication*

* ***Functionality***: Performs matrix multiplication (dot product).

* ***Requirement***: Number of columns in the first matrix must equal the number of rows in the second.

* ***Implementation***: Uses np.dot() for multiplication.

```python
# Matrix multiplication (dot product)
def multiplication(a, b):
    return np.dot(a, b)
```

*4. Matrix Subtraction*

* ***Functionality***: Subtracts the second matrix from the first, element-wise.

* ***Requirement***: Both matrices must have the same dimensions.

* ***Implementation***: Uses the - operator on NumPy arrays.

```python
# Matrix subtraction
def subtraction(a, b):
    return a - b
```

*5. Matrix Transpose*

* ***Functionality***: Converts rows into columns and vice versa.

* ***Implementation***: Uses NumPy’s .T attribute to transpose the matrix.

```python
# Transpose of a matrix
def transpose(a):
    return a.T
```

*6. Scalar Multiplication*

* ***Functionality**: Multiplies every element of a matrix by a scalar value.

* ***Implementation***: Multiplies the scalar with the NumPy array directly.

```python
# Scalar multiplication
def scalar_multiplication(scalar, A):
    return scalar * A
```

*7. Determinant Calculation*

* ***Functionality***: Computes the determinant of a square matrix.

* ***Requirement***: Matrix must be square (rows = columns).

* ***Implementation***: Uses np.linalg.det() from NumPy’s linear algebra module.

```python
# Determinant of a square matrix
def determinant(A):
    return np.linalg.det(A)
```

*8. Inverse of a Matrix*

* ***Functionality***: Calculates the inverse of a square matrix.

* ***Requirement***: Matrix must be square and non-singular (determinant ≠ 0).

* ***Implementation***: Uses np.linalg.inv().

```python
# Inverse of a square matrix
def inverse(A):
    return np.linalg.inv(A)
```

*9. Matrix Rank*

* ***Functionality***: Finds the rank of a matrix (maximum number of linearly independent row/column vectors).

* ***Implementation***: Uses np.linalg.matrix_rank().

```python
# Rank of a matrix
def rank(A):
    return np.linalg.matrix_rank(A)
```

*10. Matrix Property Checks*

* ***Symmetric Check***: Verifies if a matrix is equal to its transpose.

* ***Identity Check***: Verifies if a matrix is a square identity matrix using np.eye().

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

## 📈 Findings

* **Efficient Matrix Computation**: NumPy handles matrix operations quickly and accurately, even for large matrices.
* **User-Friendly CLI**: The menu-driven interface makes it easy for beginners to perform complex matrix tasks without deep mathematical knowledge.
* **Error Handling**: Basic validation (like shape checks for addition/multiplication) prevents runtime crashes and improves reliability.
* **Educational Value**: The project reinforces linear algebra concepts like transpose, inverse, and determinant in a hands-on way.
* **Extensibility**: The modular design allows for easy integration of advanced features like eigenvalues, LU decomposition, or visualization in the future.

## 📄 Reports

* **Operation Logs**: Outputs for each matrix operation (addition, inverse, transpose, etc.) are clearly displayed in the console for verification.
* **Matrix Validation**: The tool reports whether a matrix is square, symmetric, or an identity matrix, helping users understand its structure.
* **Error Feedback**: Informative messages are shown when operations fail (e.g., incompatible shapes or non-invertible matrices).
* **Result Accuracy**: Numerical results like determinant, rank, and inverse are displayed with precision using NumPy's built-in methods.
* **Interactive Execution**: Users can perform and view results of multiple operations in a single session, simulating a step-by-step analysis workflow.

## ✅ Conclusion

This project serves as a practical introduction to matrix operations using Python and NumPy. It helps learners understand the fundamentals of linear algebra through hands-on coding. By implementing core operations like addition, multiplication, inverse, and determinant, users build a strong foundation in both programming and mathematics. The tool's interactive and modular design makes it ideal for beginners exploring numerical computing and data science.


## 🛠️ How to Use

1. **Clone the Repository**: Clone this GitHub repository to your local machine.
2. **Install Dependencies**: Ensure Python is installed and run `pip install numpy` to install NumPy.
3. **Run the Script**: Execute the Python file using a terminal or command prompt: `python matrix_tool.py`.
4. **Follow the Menu**: Use the interactive menu to select and perform various matrix operations.
5. **Experiment Freely**: Try different matrix sizes, values, and operations to explore and learn linear algebra concepts.

## 👨‍💻Author - HARSHAVARDHAN BOMMALATA

This project is part of my portfolio, showcasing foundational Python and NumPy skills essential for roles in data science and software development. If you have any questions, feedback, or are interested in collaborating, feel free to reach out!

## 🤝 Stay Connected

* **LinkedIn**: [Connect me professionally](https://www.linkedin.com/in/harshavardhan-bommalata-7bb9442b0/)
* **Email**: [hbommalata@gmail.com](mailto:hbommalata@gmail.com) – for suggestions or collaboration
* **Instagram**: [@always\_harsha\_royal](https://www.instagram.com/always_harsha_royal/) – for personal chats

Thank you for your support! I look forward to connecting with you.
