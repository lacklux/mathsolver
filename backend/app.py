from flask import Flask, render_template, request
from solver.combinatorics import factorial, combination, permutation
from solver.quadratic import quadratic_solver
from solver.statistics import solve_median, solve_mean, solve_mode, solve_range
from solver.simple import simple_interest, compound_interest
from solver.simultaneous import equations_2, equations_3
from solver.matrices import (
    add_mat,
    subtract_mat,
    multiply_mat,
    inverse_of_matrix,
    transpose,
)
from solver.number_base import (
    base10_to_base16,
    base16_to_base10,
    base10_to_base2,
    base2_to_base10,
    base10_to_base8,
    base8_to_base10,
)
from solver.number_base import (
    binary_division,
    binary_addition,
    binary_multiplication,
    binary_subtraction,
)
import os
import re

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

app = Flask(
    __name__,
    template_folder=os.path.join(frontend_path, "templates"),
    static_folder=os.path.join(frontend_path, "static"),
)


def parser_raw(raw_value):
    try:
        return float(raw_value.strip())
    except ValueError:
        return None


def parser_matrix(raw_value):
    """
    Expects input like:
      "1,2,3;4,5,6"                 -> single matrix
      "1,2;3,4 | 5,6;7,8"           -> two matrices (split by '|')

    Returns:
      - one matrix  -> [[...], [...]]
      - two matrices -> ([[...], [...]], [[...], [...]])
    """
    try:
        # Case: two matrices separated by '|'
        if "|" in raw_value:
            parts = raw_value.split("|")
            if len(parts) != 2:
                return None  # invalid input, more than 2 matrices
            matrixA = [
                [float(x) for x in row.split(",")]
                for row in parts[0].strip().split(";")
                if row.strip()
            ]
            matrixB = [
                [float(x) for x in row.split(",")]
                for row in parts[1].strip().split(";")
                if row.strip()
            ]
            return matrixA, matrixB

        # Case: single matrix
        rows = raw_value.strip().split(";")
        matrix = [[float(x) for x in row.split(",")] for row in rows if row.strip()]
        return matrix

    except ValueError:
        return None


def parser_quadratic(raw_value):
    try:
        parts = [p.strip() for p in raw_value.strip().split(",")]
        if len(parts) != 3:
            return None, "Quadratic requires exactly 3 coefficients (a,b,c)"

        a, b, c = map(float, parts)
        if a == 0:
            return None, "Coefficient 'a' cannot be 0 in a quadratic"

        return (a, b, c), None
    except ValueError:
        return None, "Invalid quadratic coefficients"


def parser_simultaneous(raw_value):
    """
    Expects:
      - "a1,b1,c1 ; a2,b2,c2"
      - "a1,b1,c1,d1 ; a2,b2,c2,d2 ; a3,b3,c3,d3"
    Returns:
      - [[a1,b1,c1],[a2,b2,c2]]
      - [[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3]]
    """
    try:
        equations = [eq.strip() for eq in raw_value.strip().split(";") if eq.strip()]
        parsed_equations = [list(map(float, eq.split(","))) for eq in equations]

        if len(parsed_equations) == 2 and all(len(eq) == 3 for eq in parsed_equations):
            return parsed_equations  # for equations_2
        elif len(parsed_equations) == 3 and all(
            len(eq) == 4 for eq in parsed_equations
        ):
            return parsed_equations  # for equations_3
        else:
            return None  # invalid size mismatch
    except ValueError:
        return None


def parser_combinatorics(raw_value, operation):
    """
    operation: "factorial", "combination", "permutation"
    raw_value:
      - factorial: "5"
      - combination: "5,2"
      - permutation: "5,2"
    """
    try:
        if operation == "factorial":
            n = int(raw_value.strip())
            return (n,)  # tuple for factorial

        elif operation in ("combination", "permutation"):
            parts = raw_value.strip().split(",")
            if len(parts) != 2:
                return None
            n, r = map(int, parts)
            return (n, r)

        else:
            return None
    except ValueError:
        return None


def parser_number_base(raw_value, operation):
    """
    operation:
      - "base10_to_base2", "base2_to_base10",
        "base10_to_base8", "base8_to_base10",
        "base10_to_base16", "base16_to_base10"
    raw_value:
      - integer or string depending on operation
    """
    try:
        if operation.startswith("base10"):
            return int(raw_value.strip())
        elif operation.startswith("base2"):
            return raw_value.strip()
        elif operation.startswith("base8"):
            return raw_value.strip()
        elif operation.startswith("base16"):
            return raw_value.strip()
        else:
            return None
    except ValueError:
        return None


def parser_binary(raw_value):
    """
    operation: "binary_addition", "binary_subtraction",
               "binary_multiplication", "binary_division"
    raw_value: "1010,1101"
    """
    try:
        parts = raw_value.strip().split(",")
        if len(parts) != 2:
            return None
        bin1, bin2 = parts[0].strip(), parts[1].strip()
        # validation: only 0/1 allowed
        if not (set(bin1) <= {"0", "1"} and set(bin2) <= {"0", "1"}):
            return None
        return (bin1, bin2)
    except Exception:
        return None


def parser_interest(raw_value):
    """
    operation: "simple_interest", "compound_interest"
    raw_value: "1000,5,2" → (P=1000, R=5, T=2)
    """
    try:
        parts = raw_value.strip().split(",")
        if len(parts) != 3:
            return None
        P, R, T = map(float, parts)
        return (P, R, T)
    except ValueError:
        return None


def statistics_parser(raw_input: str):
    """
    Parse user input and call the appropriate statistics solver.
    Supports: mean, median, mode, range
    """
    text = raw_input.lower().strip()
    # Extract numbers from input (supports comma, spaces, etc.)
    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)
    user_numbers = [float(n) if "." in n else int(n) for n in numbers]

    if not user_numbers:
        return {"error": "No valid numbers found in input."}
    return user_numbers
  

OPTIONS = {
    "add_matrices": {
        "function": add_mat,
        "parameter": parser_matrix,
        "operation": None,
    },
    "subtract_matrices": {
        "function": subtract_mat,
        "parameter": parser_matrix,
        "operation": None,
    },
    "multiply_matrices": {
        "function": multiply_mat,
        "parameter": parser_matrix,
        "operation": None,
    },
    "inverse__matrices": {
        "function": inverse_of_matrix,
        "parameter": parser_matrix,
        "operation": None,
    },
    "transpose_matrices": {"function": transpose, "parameter": parser_matrix, "operation": None},
    "base 10 → base 16": {
        "function": base10_to_base16,
        "parameter": parser_number_base,
        "operation": "base10_to_base16",
    },
    "base 16 → base 10": {
        "function": base16_to_base10,
        "parameter": parser_number_base,
        "operation": "base16_to_base10",
    },
    "base 10 → base 2": {
        "function": base10_to_base2,
        "parameter": parser_number_base,
        "operation": "base10_to_base2",
    },
    "base 2 → base 10": {
        "function": base2_to_base10,
        "parameter": parser_number_base,
        "operation": "base2_to_base10",
    },
    "base 10 → base 8": {
        "function": base10_to_base8,
        "parameter": parser_number_base,
        "operation": "base10_to_base8",
    },
    "base 8 → base 10": {
        "function": base8_to_base10,
        "parameter": parser_number_base,
        "operation": "base8_to_base10",
    },
    "binary_division": {
        "function": binary_division,
        "parameter": parser_binary,
        "operation": "binary_division",
    },
    "binary_addition": {
        "function": binary_addition,
        "parameter": parser_binary,
        "operation": None,
    },
    "binary_multiplication": {
        "function": binary_multiplication,
        "parameter": parser_binary,
        "operation": None,
    },
    "binary_subtraction": {
        "function": binary_subtraction,
        "parameter": parser_binary,
        "operation": None,
    },
    "add_matrices": {
        "function": add_mat,
        "parameter": parser_matrix,
        "operation": None,
    },
    "median": {
        "function": solve_median,
        "parameter": statistics_parser,
        "operation": None,
    },
    "mean": {"function": solve_mean, "parameter": statistics_parser, "operation": None},
    "mode": {"function": solve_mode, "parameter": statistics_parser, "operation": None},
    "range": {
        "function": solve_range,
        "parameter": statistics_parser,
        "operation": None,
    },
    "quadratic": {
        "function": quadratic_solver,
        "parameter": parser_quadratic,
        "operation": None,
    },
    "simultaneous_2": {
        "function": equations_2,
        "parameter": parser_simultaneous,
        "operation": None,
    },
    "simultaneous_3": {
        "function": equations_3,
        "parameter": parser_simultaneous,
        "operation": None,
    },
    "simple_interest": {
        "function": simple_interest,
        "parameter": parser_interest,
        "operation": None,
    },
    "compound_interest": {
        "function": compound_interest,
        "parameter": parser_interest,
        "operation": None,
    },
    "factorial": {
        "function": factorial,
        "parameter": parser_combinatorics,
        "operation": "factorial",
    },
    "combination": {
        "function": combination,
        "parameter": parser_combinatorics,
        "operation": "combination",
    },
    "permutation": {
        "function": permutation,
        "parameter": parser_combinatorics,
        "operation": "permutation",
    },
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        select_option = request.form.get("topic")
        values = request.form.get("question", "").strip()
        calculation_type = request.form.get("calculationType")
        handler = OPTIONS.get(calculation_type)
        print(handler)
        if handler:
            function_name = handler["function"]
            parameter = handler.get("parameter")
            operation = handler.get("operation")
            if operation:
                values = parameter(values, operation)
            else:
                values = parameter(values)
            try:
                result = function_name(values)
                print(result)

            except Exception as e:
                error = f"Error occurred: {str(e)}"

        else:
            error = "Invalid calculation type selected."

    return render_template("index.html", error=error, result=result)


if __name__ == "__main__":
    app.run(debug=True)
