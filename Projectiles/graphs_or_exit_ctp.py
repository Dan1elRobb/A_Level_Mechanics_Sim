import tkinter as tk
from tkinter import messagebox
from graphing_ctp import ctp_graphs
import sys
from ctp_outputs import run_ctp_outputs


def ctp_graphs_or_exit():
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
            ctp_graphs()

        def exit_application(self):
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                sys.exit()

        def start_outputs(self):
            run_ctp_outputs()

    # Use only one instance of Tk
    root = tk.Tk()
    app = GraphsOrReRun(root)
    app.pack()  # Use pack or grid to manage geometry
    app.mainloop()
