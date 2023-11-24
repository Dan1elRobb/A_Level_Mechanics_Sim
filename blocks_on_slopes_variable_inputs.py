import easygui

message = 'Enter the question variables'
box_title = 'Blocks on slopes'
var_names = ['Mass', 'Angle', 'Friction', 'Coefficient of Friction', 'Acceleration']
var_values = []
var_values = easygui.multenterbox(message, box_title, var_names)

m = int(var_values[0])
angle = int(var_values[1])
f = int(var_values[2])
mew = float(var_values[3])
a = int(var_values[4])

print(mew)