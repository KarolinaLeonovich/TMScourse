def func_calculations(a, b):
    '''Returns sum, difference and product of two numbers'''
    sum = a + b
    difference = a - b
    product = a * b
    response_line = f"Sum is {sum}.\nDifference is {difference}.\nProduct is {product}."
    return response_line

a = float(input("Enter the first number "))
b = float(input("Enter the second number "))

print(func_calculations(a, b))