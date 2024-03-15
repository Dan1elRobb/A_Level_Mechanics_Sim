"""
This module handles the GUI that appears after the projectiles simulation and asks the user
 if they would like to produce graphs or get the variable outputs over time or exit the application entirely
"""
import tkinter as tk
from tkinter import messagebox
from Graphing_Projectiles import projectiles_graphs
import sys
from Projectile_Variables_Outputs import run_proj_outputs


def graphs_or_rerun():
    """
    This function allows this module to be run by other modules with ease
    """
    class GraphsOrReRun(tk.Frame):  # Change inheritance to tk.Frame
        """
        This class is responsible for the display of the GUI that allows user to pick between seeing the
         graphs associated with the selected question type or seeing the variables over time or exiting
         the application entirely
        Methods
        -------
        create_widgets - Creates the widgets to be displayed on the GUI (the buttons)
        produce_graphs - opens the graphs module for the question type selected
        start_outputs - opens the outputs module for the question type selected
        exit_application - uses the sys.exit() function to kill the program entirely
        All methods other than create_widgets are static
        """
        def __init__(self, master=None):
            """
            The constructor for this class calls the create_widgets method and uses the super().init call to
            define the master of the frame being the tk.Frame master
            Parameters
            ----------
            master
            """
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

        @staticmethod
        def produce_graphs():
            projectiles_graphs()

        @staticmethod
        def exit_application():
            result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
            if result == 'yes':
                sys.exit()

        @staticmethod
        def start_outputs():
            run_proj_outputs()

    # Use only one instance of Tk
    root = tk.Tk()
    app = GraphsOrReRun(root)
    app.pack()  # Use pack to manage geometry
    app.mainloop()
