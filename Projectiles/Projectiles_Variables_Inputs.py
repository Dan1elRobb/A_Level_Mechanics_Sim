import easygui
def run_inputs_proj():
    message = 'Enter the question variables'
    box_title = 'Blocks on slopes'
    var_names = ['Angle','Mass Projectile', 'Initial Velocity of Projectile',
                 'Starting Height', 'End Time']
    var_values = []
    var_values = easygui.multenterbox(message, box_title, var_names)

    with open('PVars.txt', "w") as file:
        # Iterate over the values and write each one to a new line in the file
        for value in var_values:
            file.write(value + "\n")