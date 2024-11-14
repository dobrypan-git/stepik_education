import numpy as np

def input_matrix(prompt):
    rows = int(input(f"Enter number of rows for {prompt} matrix: "))
    cols = int(input(f"Enter number of columns for {prompt} matrix: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element ({i+1},{j+1}) for {prompt} matrix: ")))
        matrix.append(row)

    return np.array(matrix)

def matrix_multiplication():
    print("Matrix Multiplication")

    A = input_matrix("A")
    B = input_matrix("B")

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    if A.shape[1] != B.shape[0]:
        print("Error: Matrices cannot be multiplied")
    else:
        C = np.dot(A, B)
        print("\nResultant Matrix C:")
        print(C)

matrix_multiplication()