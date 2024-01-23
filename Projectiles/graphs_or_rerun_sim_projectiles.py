import tkinter as tk
from tkinter import messagebox
from Projectiles_Variables_Inputs import run_inputs_proj
from Graphing_Projectiles import projectiles_graphs

class RunSimOrCancelApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Projectile Simulation")
        self.master.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        # Button to rerun the simulation
        rerun_button = tk.Button(self.master, text="Re Enter Variables", command=self.open_input_variables)
        rerun_button.pack(pady=20)

        # Button to produce graphs
        graphs_button = tk.Button(self.master, text='Graphs', command=self.produce_graphs)
        graphs_button.pack(pady=20)

        # Button to exit the application
        exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)
        exit_button.pack(pady=20)

    def open_input_variables(self):
        # Add your simulation start functionality here
        run_inputs_proj()

    def produce_graphs(self):
        projectiles_graphs()

    def exit_application(self):
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
        if result == 'yes':
            self.master.destroy()


root = tk.Tk()
app = RunSimOrCancelApp(root)
root.mainloop()