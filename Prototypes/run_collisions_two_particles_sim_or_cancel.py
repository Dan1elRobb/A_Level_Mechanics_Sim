from Collisions_simulation_two_particles import run_collision_two_particles
import tkinter as tk
from tkinter import messagebox


def run_particle_collision_sim_or_cancel():
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
            run_collision_two_particles()

        def exit_application(self):
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                self.master.destroy()

    root = tk.Tk()
    app = RunSimOrCancelApp(root)
    root.mainloop()
