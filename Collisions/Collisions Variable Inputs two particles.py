import easygui

message = 'Enter the question variables'
box_title = 'Blocks on slopes'
var_names = ['Mass Particle 1', 'Mass Particle 2', 'Velocity Particle 1', 'Velocity Particle 2',
             'Coefficient of Restitution']
var_values = []
var_values = easygui.multenterbox(message, box_title, var_names)

with open('CTPVars.txt', "w") as file:
    # Iterate over the values and write each one to a new line in the file
    for value in var_values:
        file.write(value + "\n")
