import easygui

message = 'Enter the question variables'
box_title = 'Blocks on slopes'
var_names = ['Mass', 'Angle', 'Friction', 'Coefficient of Friction', 'End Time', 'Acceleration']
var_values = []
var_values = easygui.multenterbox(message, box_title, var_names)


