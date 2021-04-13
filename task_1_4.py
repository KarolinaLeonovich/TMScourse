def func_average(numbers_array):
    '''Returns average of inputed numbers'''
    sum = 0
    for every_number in numbers_array:
        sum += every_number
    average = sum / len(numbers_array)
    return average

def func_geometric_mean(numbers_array):
    '''Returns geometric average of inputed numbers'''
    product = 1
    for each_number in numbers_array:
        product *= each_number
    geometric_average = product**(1/len(numbers_array))
    return geometric_average

numbers_array = []
print("Please enter numbers.\nEnter 'stop' to finish and look the result.")
while True:
    inputed = input()
    if inputed.isdigit():
        number = float(inputed)
        numbers_array.append(number)
    elif inputed == "stop":
        break
    else:
        print("Please check your data!")

print(func_average(numbers_array))
print(func_geometric_mean(numbers_array))



