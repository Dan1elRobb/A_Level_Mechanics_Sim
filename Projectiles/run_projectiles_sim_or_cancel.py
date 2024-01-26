from Projectiles_simulation import run_proj_sim
from Projectile_Variables_Outputs import run_proj_outputs
import tkinter as tk
from tkinter import messagebox


def run_sim_or_cancel():
    class RunSimOrCancelApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Projectile Simulation")
            self.master.geometry("300x150")

            self.create_widgets()

        def create_widgets(self):
            # Button to start the simulation
            start_button = tk.Button(self.master, text="Start Sim", command=self.start_simulation)
            start_button.pack(pady=20)

            ''' Button to start the outputs'''
            output_button = tk.Button(self.master, text="Open outputs", command=self.start_outputs)
            output_button.pack(pady=20)

            # Button to exit the application
            exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)
            exit_button.pack()

        def start_simulation(self):
            # Add your simulation start functionality here
            run_proj_sim()

        def exit_application(self):
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                self.master.destroy()

        def start_outputs(self):
            run_proj_outputs()

    root = tk.Tk()
    app = RunSimOrCancelApp(root)
    root.mainloop()
