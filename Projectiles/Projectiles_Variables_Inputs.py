import tkinter as tk
from run_projectiles_sim_or_cancel import run_sim_or_cancel

def run_inputs_proj():
    class InputWindow:
        def __init__(self, master):
            self.master = master
            self.master.title("Input Variables")

            # Default values
            self.angle_var = tk.DoubleVar(value=45.0)
            self.mass_var = tk.DoubleVar(value=1.0)
            self.initial_velocity_var = tk.DoubleVar(value=40)
            self.starting_height_var = tk.DoubleVar(value=10)
            self.end_time_var = tk.DoubleVar(value=15)

            # Labels and entry widgets
            tk.Label(master, text="Angle (degrees):").grid(row=0, column=0, padx=10, pady=5)
            self.angle_entry = tk.Entry(master, textvariable=self.angle_var)
            self.angle_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(master, text="Mass (kg):").grid(row=1, column=0, padx=10, pady=5)
            self.mass_entry = tk.Entry(master, textvariable=self.mass_var)
            self.mass_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(master, text="Initial Velocity (m/s):").grid(row=2, column=0, padx=10, pady=5)
            self.initial_velocity_entry = tk.Entry(master, textvariable=self.initial_velocity_var)
            self.initial_velocity_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(master, text="Starting Height (m):").grid(row=3, column=0, padx=10, pady=5)
            self.starting_height_entry = tk.Entry(master, textvariable=self.starting_height_var)
            self.starting_height_entry.grid(row=3, column=1, padx=10, pady=5)

            tk.Label(master, text="End Time (s):").grid(row=4, column=0, padx=10, pady=5)
            self.end_time_entry = tk.Entry(master, textvariable=self.end_time_var)
            self.end_time_entry.grid(row=4, column=1, padx=10, pady=5)

            # OK button
            tk.Button(master, text="OK", command=self.ok_button_click).grid(row=5, column=0, columnspan=2, pady=10)

        def ok_button_click(self):
            # Get the values from entry widgets and store in a list
            variables_list = [
                self.angle_var.get(),
                self.mass_var.get(),
                self.initial_velocity_var.get(),
                self.starting_height_var.get(),
                self.end_time_var.get()
            ]

            # Print the values (you can modify this part based on your use case)
            with open('PVars.txt', "w") as file:
                # Iterate over the values and write each one to a new line in the file
                for value in variables_list:
                    file.write(str(value) + "\n")
            run_sim_or_cancel()



    root = tk.Tk()
    input_window = InputWindow(root)
    root.mainloop()
