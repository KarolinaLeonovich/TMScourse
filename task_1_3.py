def func_volume_and_face(edge, unit):
    '''Returns volume and face of cube'''
    volume = edge ** 3
    face = edge ** 2
    if edge == 1:
        response_line = f"Volume is {volume} cubic {unit}.\nFace is {face} square {unit}."
    elif edge <= 0:
        response_line = "Please check your data!"
    else:
        response_line = f"Volume is {volume} cubic {unit}s.\nFace is {face} square {unit}s."
    return response_line

edge = float(input("Enter the edge of cube... "))
unit = input("Enter the units... ")

print(func_volume_and_face(edge, unit))

