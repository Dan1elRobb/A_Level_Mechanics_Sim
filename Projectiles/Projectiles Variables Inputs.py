import easygui

message = 'Enter the question variables'
box_title = 'Blocks on slopes'
var_names = ['Mass Projectile', 'Initial Velocity of Projectile',
             'Starting Height']
var_values = []
var_values = easygui.multenterbox(message, box_title, var_names)

with open('CTPVars.txt', "w") as file:
    # Iterate over the values and write each one to a new line in the file
    for value in var_values:
        file.write(value + "\n")