def solve_2_variables(a1, b1, c1, a2, b2, c2):
    steps = {}
    
    # Step 1: Record original equations
    steps["step_1"] = f"Equation 1: {a1}x + {b1}y = {c1}, Equation 2: {a2}x + {b2}y = {c2}"
    
    # Handle case where both equations are invalid
    if a1 == 0 and b1 == 0:
        return {"solution": None, "steps": {"error": "Equation 1 is invalid"}}
    if a2 == 0 and b2 == 0:
        return {"solution": None, "steps": {"error": "Equation 2 is invalid"}}

    # Eliminate x
    if a1 == 0:  # Swap equations if a1 is zero
        a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        steps["step_1_note"] = "Swapped Eq1 and Eq2 because Eq1 had no x term."
    
    factor = a2 / a1
    eq2_a = a2 - factor * a1
    eq2_b = b2 - factor * b1
    eq2_c = c2 - factor * c1
    steps["step_2"] = f"Eliminate x → New Equation 2: {eq2_a}x + {eq2_b}y = {eq2_c}"
    
    # Solve for y
    if eq2_b == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (parallel or inconsistent equations)."}}
    
    y = round(eq2_c / eq2_b, 2)
    steps["step_3"] = f"Solve for y → y = {y}"
    
    # Solve for x
    if a1 == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (x-term eliminated unexpectedly)."}}
    
    x = round((c1 - b1 * y) / a1, 2)
    steps["step_4"] = f"Substitute y into Equation 1 → x = {x}"
    
    return {"solution": (x, y), "steps": steps}


def solve_3_variables(a1, b1, c1, d1,
                      a2, b2, c2, d2,
                      a3, b3, c3, d3):
    steps = {}
    
    steps["step_1"] = f"Eq1: {a1}x + {b1}y + {c1}z = {d1}, Eq2: {a2}x + {b2}y + {c2}z = {d2}, Eq3: {a3}x + {b3}y + {c3}z = {d3}"
    
    # Handle case where first equation is invalid
    if a1 == 0 and b1 == 0 and c1 == 0:
        return {"solution": None, "steps": {"error": "Equation 1 is invalid"}}
    
    # If a1 = 0, swap equations
    if a1 == 0:
        a1, b1, c1, d1, a2, b2, c2, d2 = a2, b2, c2, d2, a1, b1, c1, d1
        steps["step_1_note"] = "Swapped Eq1 and Eq2 because Eq1 had no x term."
    
    # Eliminate x from Eq2 and Eq3
    factor2 = a2 / a1
    factor3 = a3 / a1
    eq2_b = b2 - factor2 * b1
    eq2_c = c2 - factor2 * c1
    eq2_d = d2 - factor2 * d1
    eq3_b = b3 - factor3 * b1
    eq3_c = c3 - factor3 * c1
    eq3_d = d3 - factor3 * d1
    steps["step_2"] = f"Eliminate x → Eq2: {eq2_b}y + {eq2_c}z = {eq2_d}, Eq3: {eq3_b}y + {eq3_c}z = {eq3_d}"
    
    # Eliminate y from Eq3
    if eq2_b == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (cannot eliminate y)."}}
    
    factor = eq3_b / eq2_b
    eq3_c = eq3_c - factor * eq2_c
    eq3_d = eq3_d - factor * eq2_d
    steps["step_3"] = f"Eliminate y → New Eq3: {eq3_c}z = {eq3_d}"
    
    # Solve for z
    if eq3_c == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (z-term eliminated)."}}
    
    z = round(eq3_d / eq3_c, 2)
    steps["step_4"] = f"Solve for z → z = {z}"
    
    # Back substitute for y
    if eq2_b == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (y-term eliminated)."}}
    
    y = round((eq2_d - eq2_c * z) / eq2_b, 2)
    steps["step_5"] = f"Substitute z into Eq2 → y = {y}"
    
    # Back substitute for x
    if a1 == 0:
        return {"solution": None, "steps": {**steps, "error": "No unique solution (x-term eliminated)."}}
    
    x = round((d1 - b1 * y - c1 * z) / a1, 2)
    steps["step_6"] = f"Substitute y, z into Eq1 → x = {x}"
    
    return {"solution": (x, y, z), "steps": steps}
print(solve_3_variables(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))