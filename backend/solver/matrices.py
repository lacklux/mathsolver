import numpy as np

def add_mat(matrixA,matrixB):
    a,b = np.array(matrixA),np.array(matrixB)
    if a.shape != b.shape:
        return None, "Matrix addition is not possible with these dimensions."

    rows, cols = a.shape
    result = np.zeros((rows, cols), dtype=int)
    steps = []

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
            step = f"matAB[{i+1}][{j+1}] = {a[i][j]} + {b[i][j]} = {result[i][j]}"
            steps.append(step)

    return {'Steps':steps,'Answer':result}


def subtract_mat(matrixA,matrixB):
    a,b = np.array(matrixA),np.array(matrixB)
    if a.shape != b.shape:
        return None, "Matrix subtraction is not possible with these dimensions."

    rows, cols = a.shape
    result = np.zeros((rows, cols), dtype=int)
    steps = []

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] - b[i][j]
            step = f"matAB[{i+1}][{j+1}] = {a[i][j]} - {b[i][j]} = {result[i][j]}"
            steps.append(step)

    return {'Steps':steps,'Answer':result}


def multiply_mat(matrixA,matrixB):
    a,b = np.array(matrixA),np.array(matrixB)
    rows_A, cols_A = a.shape
    rows_B, cols_B = b.shape

    if cols_A != rows_B:
        return None, "Matrix multiplication is not possible with these dimensions."

    result = np.zeros((rows_A, cols_B), dtype=int)
    steps =[]

    for i in range(rows_A):
        for j in range(cols_B):
            terms = []
            for k in range(cols_A):
                term = f"{a[i][k]}x{b[k][j]}"
                terms.append(term)
            total = sum(a[i][k] * b[k][j] for k in range(cols_A))
            result[i][j] = total
            steps.append(f"matrixAB[{i+1}][{j+1}] = {' + '.join(terms)} = {total}")
    
    return {'Steps':steps,'Answer':result}



def inverse_of_matrix(x):
    matrix =np.array(x)
    n, m = matrix.shape
    if n != m:
        raise ValueError("Matrix must be a square matrix.")

    aug = np.hstack((matrix.astype(float), np.identity(n)))
    steps = [f"Initial Augmented Matrix:\n{aug.tolist()}"]

    for i in range(n):
        pivot = aug[i, i]
        if pivot == 0:
            for j in range(i + 1, n):
                if aug[j, i] != 0:
                    aug[[i, j]] = aug[[j, i]]
                    steps.append(f"Swapped Row {i+1} with Row {j+1}")
                    steps.append(f"Matrix:\n{aug.tolist()}")
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")
            pivot = aug[i, i]

        aug[i] = aug[i] / pivot
        steps.append(f"Row {i+1} = Row {i+1} / {pivot:.2f}")
        steps.append(f"Matrix:\n{aug.tolist()}")

        for j in range(n):
            if i != j:
                factor = aug[j, i]
                if factor != 0:
                    aug[j] -= factor * aug[i]
                    steps.append(f"Row {j+1} = Row {j+1} - ({factor:.2f}) * Row {i+1}")
                    steps.append(f"Matrix:\n{aug.tolist()}")

    inverse = aug[:, n:]

    return {
        'Steps': steps,
        'Answer': inverse
    }



def transpose(x):
    matrix =np.array(x)
    rows, cols = matrix.shape
    transposed = np.zeros((cols, rows), dtype=matrix.dtype)
    steps = []

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            steps.append(
                f"matrixT[{j+1}][{i+1}] = matrix[{i+1}][{j+1}] = {matrix[i][j]}"
            )

    return {
        'Steps': steps,
        'Answer': transposed
    }

