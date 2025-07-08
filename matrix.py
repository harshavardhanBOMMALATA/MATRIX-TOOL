import numpy as np

# Function to create a matrix by taking input from the user
def matrix_creation():
    rows = int(input("\nenter rows count:"))
    columns = int(input("\nenter columns count:"))
    print("enter matrix elements(space)")
    elements = list(map(float, input().split()))
    return np.array(elements).reshape(rows, columns)

# Matrix addition
def addition(a, b):
    return a + b

# Matrix subtraction
def subtraction(a, b):
    return a - b

# Matrix multiplication (dot product)
def multiplication(a, b):
    return np.dot(a, b)

# Transpose of a matrix
def transpose(a):
    return a.T

# Scalar multiplication
def scalar_multiplication(scalar, A):
    return scalar * A

# Determinant of a square matrix
def determinant(A):
    return np.linalg.det(A)

# Inverse of a square matrix
def inverse(A):
    return np.linalg.inv(A)

# Rank of a matrix
def rank(A):
    return np.linalg.matrix_rank(A)

# Check if matrix is symmetric (A == A.T)
def array_symmetric(A):
    return np.array_equal(A, A.T)

# Check if matrix is square (rows == columns)
def check_square(A):
    return A.shape[0] == A.shape[1]

# Check if matrix is identity (square and equal to np.eye)
def is_identity(A):
    return np.array_equal(A, np.eye(A.shape[0])) if check_square(A) else False

# Menu for the user
def options():
    print("options for matrix operations")
    print("1:addition")
    print("2:subtraction")
    print("3:multiplications")
    print("4:transpose")
    print("5:scalar multiply")
    print("6:determinant")
    print("7:inverse")
    print("8:rank")
    print("9:check symmetric")
    print("10:check identity")
    print("0:exit")

# Main loop to handle user interaction
while True:
    options()
    k = int(input("enter option: "))

    # Exit
    if k == 0:
        break

    # Addition, subtraction, or multiplication
    elif k in {1, 2, 3}:
        A = matrix_creation()
        B = matrix_creation()
        if A.shape != B.shape and k != 3:
            print("addition or subtraction not possible...")
        elif A.shape == B.shape and k in {1, 2}:
            if k == 1:
                print(addition(A, B))
            else:
                print(subtraction(A, B))
        else:
            try:
                print(multiplication(A, B))
            except:
                print("multiplication not possible")

    # Transpose
    elif k == 4:
        A = matrix_creation()
        print(transpose(A))

    # Scalar multiplication
    elif k == 5:
        k = int(input("\nenter scalar value:"))
        A = matrix_creation()
        print(scalar_multiplication(k, A))

    # Determinant
    elif k == 6:
        A = matrix_creation()
        print(determinant(A))

    # Rank
    elif k == 8:
        A = matrix_creation()
        print(rank(A))

    # Inverse
    elif k == 7:
        A = matrix_creation()
        print(inverse(A))

    # Symmetric check
    elif k == 9:
        A = matrix_creation()
        if not check_square(A):
            print("Not symmetric... (matrix is not square)")
        else:
            print("Symmetric:", array_symmetric(A))

    # Identity check
    elif k == 10:
        A = matrix_creation()
        if check_square(A):
            print("Identity:", is_identity(A))
        else:
            print("Not an identity: matrix is not square")

'''------------------END---------------------------'''