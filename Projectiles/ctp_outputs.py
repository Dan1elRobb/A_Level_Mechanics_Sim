'''
This module is used to display the outputs GUI for the collisions question with two particles
Doesn't require any other modules as it is a terminating GUI and will not require any other GUI
to be opened by this one
'''

import tkinter as tk

def run_ctp_outputs():
    """
    This function allows the functionality of this module to be used by other modules when needed
    """
    class Collisions_Variable_Outputs_GUI:
        """
        This class is used for the actual display of the outputs of the collision with 2 particles question type.
        It takes in 2 lists and will loop through these lists displaying each item inside the lists at 0.01s intervals
        Attributes
        ----------
        root - This is the root of the window and allows tkinter to display the GUI and run a main
        loop through it
        particle1_vel_list - This is a list of velocities of particle 1 which is generated by the simulation module
        particle2_vel_list - This is a list of velocities of particle 2 which is generated by the simulation module
        time_list - This is a list of times at 0.01s intervals and is generated in this module

        Methods
        -------
        update_label - The method which updates the text labels every 0.01s as long as the index pointer is in range
        of the length of the shortest list generated
        close_gui - The method which destroys the root and thus closes the GUI - designed to mean that this module can
        be reused in the same instance of the progam, and it will start from the beginning of the lists when run each time
        """
        def __init__(self, root, particle1_vel_list, time_list, particle2_vel_list):
            """
            Define the root of the tkinter window and the lists of the velocities and times
            that are going to be displayed
            Parameters
            ----------
            root
            particle1_vel_list
            time_list
            particle2_vel_list
            """
            self.root = root
            self.root.title("Collisions 2 particles Outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.particle1_vel_list = particle1_vel_list
            self.time_list = time_list
            self.particle2_vel_list = particle2_vel_list
            self.current_index = 0

            # Create a label and pack it
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.particle1_vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.particle1_vel_label.pack(pady=10)
            self.particle2_vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.particle2_vel_label.pack(pady=10)

            # Create a button to close the GUI
            self.close_button = tk.Button(root, text="Close", command=self.close_gui)
            self.close_button.pack(pady=10)

            # Call the update_label method every 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)

        def update_label(self):
            """
            Update the displayed label on the output GUI with the next item in the list, keeping track
            of this using an index counter
            """
            # Get the current value from the list
            current_particle1_vel = self.particle1_vel_list[self.current_index]
            current_time = self.time_list[self.current_index]
            current_particle2_vel = self.particle2_vel_list[self.current_index]

            # Update the label with the current value
            time_display = f'Time: {str(current_time)[0:4]}'
            particle1_vel_display = f' Particle 1 Velocity: {str(current_particle1_vel)[0:5]}'
            particle2_vel_display = f'Particle 2 Velocity: {str(current_particle2_vel)[0:6]}'
            self.time_label.config(text=time_display)
            self.particle1_vel_label.config(text=particle1_vel_display)
            self.particle2_vel_label.config(text=particle2_vel_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            # Call the update_label method again after 10 milliseconds (0.01 seconds)
            if self.current_index < len(self.time_list) and self.current_index < len(self.particle2_vel_list) and self.current_index < len(self.particle1_vel_list):
                self.root.after(10, self.update_label)
            else:
                pass

        def close_gui(self):
            """
            Command function for the 'Close' button allowing the user to close the GUI
            """
            self.root.destroy()
    # Read the variables from the text file they are stored in for this particular question type and assign them
    # variables

    with open('CTPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
    # Generate the lists of the times and velocities by reading the text files where the velocities have been dumped
    times_list = []
    ct = 0
    particle1_vel_list = []
    particle2_vel_list = []
    for _ in range(100 * int(user_end_time)):
        times_list.append(ct)
        ct += 0.01
    with open('CTP1_vels.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        particle1_vel_list.append(float(l.strip()))
    with open('CTP2_vels.txt', 'r') as f:
        lin = f.readlines()
    for l in lin:
        particle2_vel_list.append(float(l.strip()))
    # Run the GUI
    root = tk.Tk()
    app = Collisions_Variable_Outputs_GUI(root, particle1_vel_list, times_list, particle2_vel_list)
    root.mainloop()


