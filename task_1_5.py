def func_hypotenuse(leg_1, leg_2):
    '''Returns hypotenuse of right triangle according the entered legs.'''
    hypotenuse = (leg_1**2 + leg_2**2)**(1/2)
    return hypotenuse

def func_triangle_area(leg_1, leg_2):
    '''Returns the area of right triangle.'''
    area = leg_1 * leg_2 / 2
    return area

leg_1 = float(input("Enter the first cathetus... "))
leg_2 = float(input("Enter the second cathetus... "))

print(func_hypotenuse(leg_1, leg_2))
print(func_triangle_area(leg_1, leg_2))