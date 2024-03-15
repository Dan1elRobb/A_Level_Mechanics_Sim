from collisions_simulation_particle_and_wall import run_collissions_wall_sim
import tkinter as tk
from tkinter import messagebox


def run_wall_collision_sim_or_cancel():
    class RunSimOrCancelApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Collisions Simulation")
            self.master.geometry("300x150")

            self.create_widgets()

        def create_widgets(self):
            # Button to start the simulation
            start_button = tk.Button(self.master, text="Start Sim", command=self.start_simulation)
            start_button.pack(pady=20)

            # Button to exit the application
            exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)
            exit_button.pack()

        def start_simulation(self):
            # Add your simulation start functionality here
            run_collissions_wall_sim()

        def exit_application(self):
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                self.master.destroy()

    root = tk.Tk()
    app = RunSimOrCancelApp(root)
    root.mainloop()