def func_formula(x, y):
    '''Prints some weird calculation)'''
    result = (abs(x) - abs(y)) / (1 + abs(x * y))
    result_line = f"Result is {result}."
    print(result_line)

x = float(input("Enter the first number "))
y = float(input("Enter the second number "))

func_formula(x, y)