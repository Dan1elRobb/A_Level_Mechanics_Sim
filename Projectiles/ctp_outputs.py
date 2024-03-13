import tkinter as tk

import math

def run_ctp_outputs():
    class Projectiles_Variable_Outputs_GUI:
        def __init__(self, root, particle1_vel_list, time_list, particle2_vel_list):
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

            # Call the update_label method again after 1000 milliseconds (1 second)
            if self.current_index < len(self.time_list) and self.current_index < len(self.particle2_vel_list) and self.current_index < len(self.particle1_vel_list):
                self.root.after(10, self.update_label)
            else:
                pass

        def close_gui(self):
            self.root.destroy()

    with open('CTPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
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

    root = tk.Tk()
    app = Projectiles_Variable_Outputs_GUI(root, particle1_vel_list, times_list, particle2_vel_list)
    root.mainloop()


