import math

def simple_interest(P, R, T):
    ans = {
        "steps": {}
    }

    
    ans["steps"]["step_1"] = "Formula: SI = (P × R × T) / 100"

    
    ans["steps"]["step_2"] = f"Substitute values: SI = ({P} × {R} × {T}) / 100"

    
    SI = (P * R * T) / 100
    ans["steps"]["step_3"] = f"Calculate: SI = {SI}"

    ans["solution"] = SI

    return ans




def compound_interest(P, R, T):
    ans = {
        "steps": {}
    }

  
    ans["steps"]["step_1"] = "Formula: A = P × (1 + R/100)^T"

    
    ans["steps"]["step_2"] = f"Substitute values: A = {P} × (1 + {R}/100)^{T}"

    
    A = P * (1 + R/100) ** T
    ans["steps"]["step_3"] = f"Calculate final amount: A = {round(A, 2)}"

    
    CI = A - P
    ans["steps"]["step_4"] = f"Compound Interest: CI = A - P = {round(CI, 2)}"

    
    ans["solution"] = round(CI, 2)

    return ans
