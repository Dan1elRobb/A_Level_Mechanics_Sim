'''
This is the module which is used to display the GUI that pops up after the Blocks on Slopes simulation
has finished and allows the user to generate the graph associated with the question type or to open the
outputs over time window

Makes use of the graphing_bons module to display the graphs GUI and the Blocks_on_slopes_variables_outputs
module to display the outputs GUI
'''
import tkinter as tk
from tkinter import messagebox
from graphing_bons import bons_graphs
import sys
from Blocks_on_slopes_variables_outputs import run_bons_outputs

def bons_graphs_or_exit():
    """
    This function allows this module to be executed by the simulation module such that there will be
    no delay between the simulation ending and this GUI popping up
    """
    class GraphsOrExit(tk.Frame):  # Change inheritance to tk.Frame
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.create_widgets()

        def create_widgets(self):
            """
            This function will create the widgets that area going to be displayed in the GUI
            """
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
            """
            This function is the command for the 'Graphs' button and makes use of the graphing_bons module
            to display the graphs associated with the question type
            """
            bons_graphs()

        def exit_application(self):
            """
            This function is the command for the 'Exit' button and makes use of the inbuilt messagebox from
            tkinter that allows the user to give confirmation when exiting in case of a misclick
            Makes use of the imported sys module to kill the program entirely if the exit button is clicked
            """
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                sys.exit()

        def start_outputs(self):
            """
            This function is the command for the 'Show Variables Over Time' button and makes use of te
            Blocks_on_slopes_variables_outputs module to display the outputs GUI
            """
            run_bons_outputs()

    # Use only one instance of Tk
    root = tk.Tk()
    app = GraphsOrExit(root)
    app.pack()  # Use pack to manage geometry
    app.mainloop()
