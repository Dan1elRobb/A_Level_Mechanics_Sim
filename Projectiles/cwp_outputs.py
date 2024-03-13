import tkinter as tk
import math


def run_cwp_outputs():
    class Projectiles_Variable_Outputs_GUI:
        def __init__(self, root, particle_vel_list, time_list):
            self.root = root
            self.root.title("Collisions particle and wall outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.particle_vel_list = particle_vel_list
            self.time_list = time_list
            self.current_index = 0

            # Create a label and pack it
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.particle_vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.particle_vel_label.pack(pady=10)

            # Create a button to close the GUI
            self.close_button = tk.Button(root, text="Close", command=self.close_gui)
            self.close_button.pack(pady=10)

            # Call the update_label method every 1000 milliseconds (1 second)
            if self.current_index < len(self.time_list) and self.current_index < len(
                    self.particle_vel_list):
                self.root.after(10, self.update_label)
            else:
                pass

        def update_label(self):
            # Get the current value from the list
            current_particle_vel = self.particle_vel_list[self.current_index]
            current_time = self.time_list[self.current_index]


            # Update the label with the current value
            time_display = f'Time: {str(current_time)[0:4]}'
            particle_vel_display = f' Particle Velocity: {str(current_particle_vel)[0:5]}'
            self.time_label.config(text=time_display)
            self.particle_vel_label.config(text=particle_vel_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            # Call the update_label method again after 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)

        def close_gui(self):
            self.root.destroy()
    with open('CWPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
    times_list = []
    ct = 0
    particle_vel_list = []

    for _ in range(100 * int(user_end_time)):
        times_list.append(ct)
        ct += 0.01
    with open('CWP_vels.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        particle_vel_list.append(float(l.strip()))
    root = tk.Tk()
    app = Projectiles_Variable_Outputs_GUI(root, particle_vel_list,times_list)
    root.mainloop()



