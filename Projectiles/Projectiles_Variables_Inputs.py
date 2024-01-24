import tkinter as tk
from run_projectiles_sim_or_cancel import run_sim_or_cancel
from tkinter import ttk


class WelcomeScreen(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        self.configure(bg='#f0f0f0')  # Set background color

        # Welcome Label
        welcome_label = ttk.Label(self, text='Welcome to the Mechanics simulator', font=('Helvetica', 16),
                                  background='#f0f0f0')
        welcome_label.pack(pady=20)

        # Button Frame
        button_frame = ttk.Frame(self, padding=10, style='Button.TFrame')  # Using a ttk Frame with a custom style
        button_frame.pack()

        # Buttons
        blocks_button = ttk.Button(button_frame, text='Blocks on Slopes', command=self.blocks_button_clicked)
        blocks_button.grid(row=0, column=0, padx=10, pady=10)

        collisions_button = ttk.Button(button_frame, text='Collisions', command=self.collisions_button_clicked)
        collisions_button.grid(row=0, column=1, padx=10, pady=10)

        projectiles_button = ttk.Button(button_frame, text='Projectiles', command=self.projectiles_button_clicked)
        projectiles_button.grid(row=0, column=2, padx=10, pady=10)

        # Custom style for the Frame to set the background color
        self.style = ttk.Style()
        self.style.configure('Button.TFrame', background='#f0f0f0')

    def blocks_button_clicked(self):
        # Placeholder for the functionality when the "Blocks on Slopes" button is clicked
        print('BONS')

    def collisions_button_clicked(self):
        # Placeholder for the functionality when the "Collisions" button is clicked
        print('C')

    def projectiles_button_clicked(self):
        # Placeholder for the functionality when the "Projectiles" button is clicked
        self.switch_frame_callback(ProjInputWindow)

class ProjInputWindow(tk.Frame):
    def __init__(self,master,switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.angle_var = tk.DoubleVar(value=45.0)
        self.mass_var = tk.DoubleVar(value=1.0)
        self.initial_velocity_var = tk.DoubleVar(value=40)
        self.starting_height_var = tk.DoubleVar(value=10)
        self.end_time_var = tk.DoubleVar(value=15)

        # Labels and entry widgets
        ttk.Label(self, text="Angle (degrees):").grid(row=0, column=0, padx=10, pady=5)
        self.angle_entry = tk.Entry(self, textvariable=self.angle_var)
        self.angle_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Mass (kg):").grid(row=1, column=0, padx=10, pady=5)
        self.mass_entry = tk.Entry(self, textvariable=self.mass_var)
        self.mass_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Velocity (m/s):").grid(row=2, column=0, padx=10, pady=5)
        self.initial_velocity_entry = tk.Entry(self, textvariable=self.initial_velocity_var)
        self.initial_velocity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Starting Height (m):").grid(row=3, column=0, padx=10, pady=5)
        self.starting_height_entry = tk.Entry(self, textvariable=self.starting_height_var)
        self.starting_height_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self, text="End Time (s):").grid(row=4, column=0, padx=10, pady=5)
        self.end_time_entry = tk.Entry(self, textvariable=self.end_time_var)
        self.end_time_entry.grid(row=4, column=1, padx=10, pady=5)

        # OK button
        ttk.Button(self, text="OK", command=self.ok_button_click).grid(row=5, column=0, columnspan=2, pady=10)

        # Back button
        ttk.Button(self,text='Go back', command=self.back_button_click).grid(row=6, column=0, columnspan=2, pady=10)

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

    def back_button_click(self):
        self.switch_frame_callback(WelcomeScreen)


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dans Mechanics Sim")
        self.geometry("400x300")

        self.current_frame = None
        self.switch_frame(WelcomeScreen)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.switch_frame)

        if self.current_frame:
            self.current_frame.destroy()

        new_frame.pack(fill="both", expand=True)
        self.current_frame = new_frame


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
