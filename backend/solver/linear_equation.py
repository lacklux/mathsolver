import matplotlib.pyplot as plt
import numpy as np
import os

def solve_linear(m, c, filename="linear_equation.png", folder="../../frontend/static", show_graph=False):
    steps = {}

    
    steps["Step 1"] = f"Equation: y = {m}x + {c}"

    steps["Step 2"] = f"Slope (m) = {m}, Intercept (c) = {c}"

    y_intercept = c
    steps["Step 3"] = f"When x = 0 → y = {m}(0) + {c} = {y_intercept}"

    if m != 0:
        x_intercept = -c / m
        steps["Step 4"] = f"When y = 0 → 0 = {m}x + {c} → x = {-c}/{m} = {x_intercept}"
    else:
        x_intercept = None
        steps["Step 4"] = "Slope m = 0, line is horizontal, no x-intercept."

    os.makedirs(folder, exist_ok=True)
    save_path = os.path.join(folder, filename)

    
    steps["Step 5"] = f"Graph saved as '{save_path}'."

    # Plot Graph
    x = np.linspace(-10, 10, 200)
    y = m * x + c

    plt.axhline(0, color='black', linewidth=0.8)  # x-axis
    plt.axvline(0, color='black', linewidth=0.8)  # y-axis
    plt.plot(x, y, label=f"y = {m}x + {c}", color="blue")
    plt.scatter(0, y_intercept, color="red", label=f"y-intercept (0, {y_intercept})")
    if x_intercept is not None:
        plt.scatter(x_intercept, 0, color="green", label=f"x-intercept ({x_intercept}, 0)")

    plt.title("Graph of Linear Equation")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.grid(True)

    # Save graph in your folder
    plt.savefig(save_path, dpi=300, bbox_inches="tight")

    if show_graph:
        plt.show()

    plt.close()

    return {"solution": [x_intercept, y_intercept], "steps": steps}
