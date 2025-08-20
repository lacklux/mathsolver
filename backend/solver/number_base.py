# Number Base Conversion.

# 1. Convert base 10 → base 2
def base10_to_base2(number):
    steps = {}
    n = number
    bits = []
    step_no = 1
    while n > 0:
        n, remainder = divmod(n, 2)
        bits.append(str(remainder))
        steps[f"step_{step_no}"] = f"divide by 2 → quotient = {n}, remainder = {remainder}"
        step_no += 1
    bits.reverse()
    result = ''.join(bits) if bits else '0'
    return {"solution": result, "steps": steps, "base": 2}


print(base10_to_base2(25))


# 2. Convert base 2 → base 10
def base2_to_base10(binary_str):
    steps = {}
    total = 0
    power = 0
    step_no = 1
    for digit in binary_str[::-1]:  
        value = int(digit)
        part_value = value * (2 ** power)
        steps[f"step_{step_no}"] = f"Digit {digit} × 2^{power} = {part_value}"
        total += part_value
        power += 1
        step_no += 1
    return {"solution": total, "steps": steps, "base": 10}


print(base2_to_base10("11001"))


# 3. Convert base 10 → base 8
def base10_to_base8(number):
    steps = {}
    n = number
    oct_digits = []
    step_no = 1
    while n > 0:
        n, remainder = divmod(n, 8)
        oct_digits.append(str(remainder))
        steps[f"step_{step_no}"] = f"Divide by 8 → quotient = {n}, remainder = {remainder}"
        step_no += 1
    oct_digits.reverse()
    result = ''.join(oct_digits) if oct_digits else '0'
    return {"solution": result, "steps": steps, "base": 8}


print(base10_to_base8(83))


# 4. Convert base 8 → base 10
def base8_to_base10(octal_str):
    steps = {}
    total = 0
    power = 0
    step_no = 1
    for digit in octal_str[::-1]: 
        value = int(digit)
        part_value = value * (8 ** power)
        steps[f"step_{step_no}"] = f"Digit {digit} × 8^{power} = {part_value}"
        total += part_value
        power += 1
        step_no += 1
    return {"solution": total, "steps": steps, "base": 10}


print(base8_to_base10("123"))


# 5. Convert base 10 → base 16
def base10_to_base16(number):
    steps = {}
    digits = '0123456789ABCDEF'
    n = number
    hex_digits = []
    step_no = 1
    while n > 0:
        n, remainder = divmod(n, 16)
        hex_digits.append(digits[remainder])
        steps[f"step_{step_no}"] = f"Divide by 8 → quotient = {n}, remainder = {remainder}"
        step_no += 1
    hex_digits.reverse()
    result = ''.join(hex_digits) if hex_digits else '0'
    return {"solution": result, "steps": steps, "base": 16}

print(base10_to_base16(255))


# 6. Convert base 16 → base 10
def base16_to_base10(hex_str):
    steps = {}
    digits = '0123456789ABCDEF'
    total = 0
    power = 0
    step_no = 1
    for digit in hex_str[::-1].upper(): 
        value = digits.index(digit)
        part_value = value * (16 ** power)
        steps[f"step_{step_no}"] = f"Digit {digit} × 16^{power} = {part_value}"
        total += part_value
        power += 1
        step_no += 1
    return {"solution": total, "steps": steps, "base": 10}


print(base16_to_base10("FF"))


# BINARY ADDITION
def binary_addition(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    while len(bin1) < max_len:
        bin1 = "0" + bin1
    while len(bin2) < max_len:
        bin2 = "0" + bin2

    result = ""
    carry = 0
    steps = {}
    step_no = 1

    for i in range(max_len - 1, -1, -1):
        b1 = int(bin1[i])
        b2 = int(bin2[i])
        total = b1 + b2 + carry

        if total == 0:
            result = "0" + result
            carry = 0
            steps[f"step_{step_no}"] = f"{b1} + {b2} + carry {carry} = 0 (carry=0)"
        elif total == 1:
            result = "1" + result
            carry = 0
            steps[f"step_{step_no}"] = f"{b1} + {b2} + carry {carry} = 1 (carry=0)"
        elif total == 2:
            result = "0" + result
            carry = 1
            steps[f"step_{step_no}"] = f"{b1} + {b2} + carry {carry} = 10 (sum=0, carry=1)"
        elif total == 3:
            result = "1" + result
            carry = 1
            steps[f"step_{step_no}"] = f"{b1} + {b2} + carry {carry} = 11 (sum=1, carry=1)"

        step_no += 1

    if carry == 1:
        result = "1" + result
        steps[f"step_{step_no}"] = "Final carry = 1 → add to the front"

    return {
        "solution": result,
        "steps": steps,
        "operation": "binary_addition"
    }


print(binary_addition("1011", "1101"))

# BINARY SUBTRACTION
def binary_subtraction(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    while len(bin1) < max_len:
        bin1 = "0" + bin1
    while len(bin2) < max_len:
        bin2 = "0" + bin2

    result = ""
    borrow = 0
    steps = {}
    step_no = 1

    for i in range(max_len - 1, -1, -1):
        b1 = int(bin1[i]) - borrow
        b2 = int(bin2[i])

        if b1 < b2:   
            b1 += 2
            borrow = 1
            diff = b1 - b2
            steps[f"step_{step_no}"] = f"{bin1[i]} - {bin2[i]} (with borrow) = {diff}, borrow=1"
        else:
            diff = b1 - b2
            borrow = 0
            steps[f"step_{step_no}"] = f"{bin1[i]} - {bin2[i]} = {diff}, borrow=0"

        result = str(diff) + result
        step_no += 1

    result = result.lstrip("0") or "0"

    return {
        "solution": result,
        "steps": steps,
        "operation": "binary_subtraction"
    }

print(binary_subtraction("1101", "1011"))


# BINARY MULTIPLICATION

def binary_multiplication(bin1, bin2):
    steps = {}
    step_no = 1

    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    steps[f"step_{step_no}"] = f"Convert {bin1} → {dec1}, {bin2} → {dec2}"
    step_no += 1

    product = dec1 * dec2
    steps[f"step_{step_no}"] = f"Multiply decimals: {dec1} × {dec2} = {product}"
    step_no += 1

    bin_product = bin(product)[2:]  
    steps[f"step_{step_no}"] = f"Convert product {product} → binary = {bin_product}"

    return {
        "solution": bin_product,
        "steps": steps,
        "operation": "binary_multiplication"
    }
print(binary_multiplication("101", "11"))



# BINARY DIVISION

def binary_division(bin1, bin2):
    steps = {}
    step_no = 1

    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    steps[f"step_{step_no}"] = f"Convert {bin1} → {dec1}, {bin2} → {dec2}"
    step_no += 1

    quotient = dec1 // dec2
    remainder = dec1 % dec2
    steps[f"step_{step_no}"] = f"Divide decimals: {dec1} ÷ {dec2} → quotient={quotient}, remainder={remainder}"
    step_no += 1

    bin_quotient = bin(quotient)[2:]
    bin_remainder = bin(remainder)[2:]
    steps[f"step_{step_no}"] = f"Convert quotient {quotient} → binary = {bin_quotient}"
    step_no += 1
    steps[f"step_{step_no}"] = f"Convert remainder {remainder} → binary = {bin_remainder}"

    return {
        "solution": {"quotient": bin_quotient, "remainder": bin_remainder},
        "steps": steps,
        "operation": "binary_division"
    }
print(binary_division("1110", "10"))