import tkinter as tk
from tkinter import ttk
from blocks_on_slopes_simulation import Sim


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Graph or ReRun')
        self.geometry('1280x720')

        self.label = ttk.Label(self, text='Graphs Or Rerun')
        self.label.pack()

        self.graphs_button = ttk.Button(self, text='Graphs', command=self.graphs_button_clicked)
        self.graphs_button.pack()

        self.rerun_button = ttk.Button(self, text='ReRun Simulation', command=self.rerun_button_clicked)
        self.rerun_button.pack()

        # Create an instance of VelocityTimeGraphFrame but don't pack it yet


        # Initialize Sim instance here
        self.sim_instance = None

    def rerun_button_clicked(self):
        # Check if the Sim instance is already created
        if self.sim_instance is None:
            self.sim_instance = Sim()

        # Call run method on the Sim instance
        self.sim_instance.run()

    def graphs_button_clicked(self):
        # Pack the VelocityTimeGraphFrame instance created in __init__
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
