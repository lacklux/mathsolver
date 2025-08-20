import math

def quadratic_solver(a, b, c):
    steps = {}  

    steps["Step 1"] = f"Equation: {a}x^2 + {b}x + {c} = 0"

    
    discriminant = b**2 - 4*a*c
    steps["Step 2"] = f"Discriminant = {b}^2 - 4({a})({c}) = {discriminant}"

   
    if discriminant < 0:
        steps["Step 3"] = "Discriminant < 0 → No real roots."
    else:
        sqrt_disc = math.sqrt(discriminant)
        steps["Step 3"] = f"Square root of discriminant = √{discriminant} = {sqrt_disc}"

       
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)

        steps["Step 4"] = f"x1 = (-{b} + √{discriminant}) / (2*{a}) = {x1}"
        steps["Step 5"] = f"x2 = (-{b} - √{discriminant}) / (2*{a}) = {x2}"
    

        
    return {'solution':[x1,x2],'steps':steps}







result = quadratic_solver(1, -3, 2)

for step, detail in result.items():
    print(f"{step}: {detail}")
