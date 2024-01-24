import tkinter as tk
import math


def run_proj_outputs():
    class Projectiles_Variable_Outputs_GUI:
        def __init__(self, root, y_vel_list, time_list, y_dis_list, x_dis_list):
            self.root = root
            self.root.title("Blocks On Slopes Variable Outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.y_vel_list = y_vel_list
            self.time_list = time_list
            self.x_dis_list = x_dis_list
            self.y_dis_list = y_dis_list
            self.current_index = 0

            # Create a label and pack it
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.y_vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.y_vel_label.pack(pady=10)
            self.x_dis_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.x_dis_label.pack(pady=10)
            self.y_dis_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.y_dis_label.pack(pady=10)

            # Call the update_label method every 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)

        def update_label(self):
            # Get the current value from the list
            current_y_vel = self.y_vel_list[self.current_index]
            current_time = self.time_list[self.current_index]
            current_x_dis = self.x_dis_list[self.current_index]
            current_y_dis = self.y_dis_list[self.current_index]

            # Update the label with the current value
            y_vel_display = f' Y Velocity: {str(current_y_vel)[0:5]}'
            time_display = f'Time: {str(current_time)[0:4]}'
            x_dis_display = f'X Displacement: {str(current_x_dis)[0:6]}'
            y_dis_display = f'Y Displacement: {str(current_y_dis)[0:6]}'
            self.y_vel_label.config(text=y_vel_display)
            self.time_label.config(text=time_display)
            self.x_dis_label.config(text=x_dis_display)
            self.y_dis_label.config(text=y_dis_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            # Call the update_label method again after 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)

    with open('PVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_angle = float(file.readline().strip())
        user_mass = float(file.readline().strip())
        user_initial_vel = float(file.readline().strip())
        user_starting_height = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
        # Simulation setup
    mass = user_mass
    angle = user_angle  # Initial angle in degrees
    start_height = user_starting_height
    initial_velocity = user_initial_vel  # Adjust the initial speed as needed

    def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
        t = 0
        time_list = []
        y_dis_list = []
        x_dis_list = []
        y_vel_list = []
        while t < end_time:
            y_s = initial_vel * math.sin(angle) * t - 4.9 * t ** 2 + initial_height
            x_s = initial_vel * math.cos(angle) * t
            y_vel = initial_vel * math.sin(angle) - 9.8 * t
            y_dis_list.append(y_s)
            x_dis_list.append(x_s)
            y_vel_list.append(y_vel)
            time_list.append(t)
            t += 0.01
        return time_list, y_dis_list, x_dis_list, y_vel_list

    time_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[0]
    y_dis_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[1]
    x_dis_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[2]
    y_vel_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[3]

    root = tk.Tk()
    app = Projectiles_Variable_Outputs_GUI(root, y_vel_list, time_list, y_dis_list, x_dis_list)
    root.mainloop()



