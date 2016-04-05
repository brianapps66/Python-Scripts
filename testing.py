values = [[['19138'], ['b']], [['0'], ['c']]]
print(values)
values = [item for sublist in values for item in sublist]
print(values)

input_wire = [values[i][0][0] for i in range(len(values)) if values[i][1][
    0]=='b']
print('input_wire: ',input_wire)
print('input_wire: ',input_wire[0])
print(type(input_wire[0]))
