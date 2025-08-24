import numpy as np
from fractions import Fraction

def to_latex_matrix(matrix, as_fraction=True, precision=3):
    """Convert a 2D numpy array (or list of lists) to LaTeX bmatrix format."""
    matrix = np.array(matrix)
    rows = []

    for row in matrix:
        formatted_row = []
        for val in row:
            if as_fraction:
                try:
                    frac = Fraction(val).limit_denominator(1000)
                    if frac.denominator == 1:
                        formatted_row.append(str(frac.numerator))
                    else:
                        formatted_row.append(f"\\tfrac{{{frac.numerator}}}{{{frac.denominator}}}")
                except Exception:
                    formatted_row.append(str(round(float(val), precision)))
            else:
                formatted_row.append(str(round(float(val), precision)))
        rows.append(" & ".join(formatted_row))

    body = " \\\\ ".join(rows)
    return f"\\begin{{bmatrix}} {body} \\end{{bmatrix}}"


def add_mat(matrixA, matrixB):
    a, b = np.array(matrixA), np.array(matrixB)
    if a.shape != b.shape:
        return {"solution": None, "steps": {"error": "Matrix addition is not possible with these dimensions."}}

    rows, cols = a.shape
    result = np.zeros((rows, cols), dtype=int)
    steps = {}
    step_no = 1

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
            steps[f"step_{step_no}"] = f"matAB[{i+1}][{j+1}] = {a[i][j]} + {b[i][j]} = {result[i][j]}"
            step_no += 1

    return {
        "solution": to_latex_matrix(result),
        "steps": steps
    }


def subtract_mat(matrixA, matrixB):
    a, b = np.array(matrixA), np.array(matrixB)
    if a.shape != b.shape:
        return {"solution": None, "steps": {"error": "Matrix subtraction is not possible with these dimensions."}}

    rows, cols = a.shape
    result = np.zeros((rows, cols), dtype=int)
    steps = {}
    step_no = 1

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] - b[i][j]
            steps[f"step_{step_no}"] = f"matAB[{i+1}][{j+1}] = {a[i][j]} - {b[i][j]} = {result[i][j]}"
            step_no += 1

    return {
        "solution": to_latex_matrix(result),
        "steps": steps
    }


def multiply_mat(matrixA, matrixB):
    a, b = np.array(matrixA), np.array(matrixB)
    rows_A, cols_A = a.shape
    rows_B, cols_B = b.shape

    if cols_A != rows_B:
        return {"solution": None, "steps": {"error": "Matrix multiplication is not possible with these dimensions."}}

    result = np.zeros((rows_A, cols_B), dtype=int)
    steps = {}
    step_no = 1

    for i in range(rows_A):
        for j in range(cols_B):
            terms = []
            for k in range(cols_A):
                terms.append(f"{a[i][k]}×{b[k][j]}")
            total = sum(a[i][k] * b[k][j] for k in range(cols_A))
            result[i][j] = total
            steps[f"step_{step_no}"] = f"matrixAB[{i+1}][{j+1}] = {' + '.join(terms)} = {total}"
            step_no += 1

    return {
        "solution": to_latex_matrix(result),
        "steps": steps
    }


def transpose(matrixA):
    matrix = np.array(matrixA)
    rows, cols = matrix.shape
    transposed = np.zeros((cols, rows), dtype=matrix.dtype)
    steps = {}
    step_no = 1

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            steps[f"step_{step_no}"] = f"matrixT[{j+1}][{i+1}] = matrix[{i+1}][{j+1}] = {matrix[i][j]}"
            step_no += 1

    return {
        "solution": to_latex_matrix(transposed),
        "steps": steps
    }


def inverse_of_matrix(x):
    matrix = np.array(x)
    n, m = matrix.shape
    if n != m:
        raise ValueError("Matrix must be a square matrix.")

    aug = np.hstack((matrix.astype(float), np.identity(n)))
    steps = {}
    step_no = 1

    steps[f"step_{step_no}"] = f"Initial Augmented Matrix: {to_latex_matrix(aug)}"
    step_no += 1

    for i in range(n):
        pivot = aug[i, i]
        if pivot == 0:
            for j in range(i + 1, n):
                if aug[j, i] != 0:
                    aug[[i, j]] = aug[[j, i]]
                    steps[f"step_{step_no}"] = f"Swapped Row {i+1} with Row {j+1} → {to_latex_matrix(aug)}"
                    step_no += 1
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")
            pivot = aug[i, i]

        aug[i] = aug[i] / pivot
        steps[f"step_{step_no}"] = f"Row {i+1} = Row {i+1} / {pivot:.2f} → {to_latex_matrix(aug)}"
        step_no += 1

        for j in range(n):
            if i != j:
                factor = aug[j, i]
                if factor != 0:
                    aug[j] -= factor * aug[i]
                    steps[f"step_{step_no}"] = f"Row {j+1} = Row {j+1} - ({factor:.2f}) * Row {i+1} → {to_latex_matrix(aug)}"
                    step_no += 1

    inverse = aug[:, n:]

    return {
        'steps': steps,
        'solution': to_latex_matrix(inverse)
    }
