import tkinter as tk
import math


def run_bons_outputs():
    class Blocks_on_slopes_Variable_Outputs_GUI:
        def __init__(self, root, vel_list, time_list):
            self.root = root
            self.root.title("Blocks On Slopes Variable Outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.vel_list = vel_list
            self.time_list = time_list
            self.current_index = 0

            # Create a label and pack it
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.vel_label.pack(pady=10)

            # Call the update_label method every 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)

        def update_label(self):
            # Get the current value from the list
            current_vel = self.vel_list[self.current_index]
            current_time = self.time_list[self.current_index]

            # Update the label with the current value
            vel_display = f'Velocity: {str(current_vel)[0:5]}'
            time_display = f'Time: {str(current_time)[0:4]}'
            self.vel_label.config(text=vel_display)
            self.time_label.config(text=time_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            # Call the update_label method again after 1000 milliseconds (1 second)
            self.root.after(10, self.update_label)


    def calc_v_over_time(angle, mew, end_time):
        t = 0
        time_list = []
        vel_list = []
        while t < end_time:
            v = 9.8 * t * (math.sin(angle) - math.cos(angle) * mew)
            vel_list.append(v)
            time_list.append(t)
            t += 0.01
        return vel_list, time_list

    with open('BOSVars.txt', "r") as file:
        # Read each line and assign values to variables
        mass = float(file.readline().strip())
        angle = float(file.readline().strip())
        mew = float(file.readline().strip())
        end_time = float(file.readline().strip())


    vel_list = calc_v_over_time(math.radians(angle), mew, end_time)[0]
    time_list = calc_v_over_time(math.radians(angle), mew, end_time)[1]

    root = tk.Tk()
    app = Blocks_on_slopes_Variable_Outputs_GUI(root, vel_list, time_list)
    root.mainloop()
