def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def floor_divide(a, b):
    return a // b

def modulo(a, b):
    return a % b

def power(a, b):
    return a ** b

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal