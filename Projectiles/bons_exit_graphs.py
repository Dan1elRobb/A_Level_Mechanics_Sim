import tkinter as tk
from tkinter import messagebox
from graphing_bons import bons_graphs
import sys
from Blocks_on_slopes_variables_outputs import run_bons_outputs

def bons_graphs_or_exit():
    class GraphsOrReRun(tk.Frame):  # Change inheritance to tk.Frame
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.create_widgets()

        def create_widgets(self):
            # Button to produce graphs
            graphs_button = tk.Button(self, text='Graphs', command=self.produce_graphs)
            graphs_button.pack(pady=20)

            # Button to run outputs
            outputs_button = tk.Button(self, text='Show Variables Over Time', command=self.start_outputs)
            outputs_button.pack(pady=20)

            # Button to exit the application
            exit_button = tk.Button(self, text="Exit", command=self.exit_application)
            exit_button.pack(pady=20)

        def produce_graphs(self):
            bons_graphs()

        def exit_application(self):
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                sys.exit()

        def start_outputs(self):
            run_bons_outputs()

    # Use only one instance of Tk
    root = tk.Tk()
    app = GraphsOrReRun(root)
    app.pack()  # Use pack or grid to manage geometry
    app.mainloop()
