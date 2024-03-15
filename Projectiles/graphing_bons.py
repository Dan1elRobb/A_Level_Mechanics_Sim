"""
This module is used to display the graphs associated with the Blocks on slopes question type
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math


def bons_graphs():
    """
    This function is used so the graphs module can be run from another module with ease
    """
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('BOSVars.txt', "r") as file:
        # Read each line and assign values to variables
        mass = float(file.readline().strip())
        angle = float(file.readline().strip())
        mew = float(file.readline().strip())
        end_time = float(file.readline().strip())

    def calc_v_over_time(angle, mew, end_time):
        """
        This function takes in the users inputted values and calculates a list of velocities for the blocks
        also generates a list of times at 0.01s intervals
        Parameters
        ----------
        angle
        mew
        end_time

        Returns
        -------
        List of lists - [vel_list,time_list]
        """
        t = 0
        time_list = []
        vel_list = []
        while t < end_time:
            v = 9.8 * t * (math.sin(angle) - math.cos(angle) * mew)
            vel_list.append(v)
            time_list.append(t)
            t += 0.01
        return vel_list, time_list
    # Generate the veloctiy and time lists using the above function
    vel_list = calc_v_over_time(math.radians(angle), mew, end_time)[0]
    time_list = calc_v_over_time(math.radians(angle), mew, end_time)[1]

    class GraphsApp(tk.Tk):
        """
        This class is responsible for the main window of the graphs display - all graphs that will be displayed
        (currently only one) can be stuck on to this window
        """
        def __init__(self):
            super().__init__()
            self.title('Blocks on slopes graphs')

            y_vel_graph_page = VelocityTimeGraphFrame(self, "Velocity vs Time")

            y_vel_graph_page.pack(padx=10)

    class VelocityTimeGraphFrame(tk.Frame):
        """
        This class is responsible for the creation of the frame which will display the velocity vs time
        graph and be stuck onto the main application
        """

        def __init__(self, master, title):
            """
            Constructor of the class which defines the master of the frame and the title for the graph
            Parameters
            ----------
            master
            title
            """
            super().__init__(master)
            self.title = title
            self.create_graph()

        def create_graph(self):
            """
            This method uses the matplotlib library to create the graphs based on lists of variable generated
            """
            fig = plt.figure(figsize=(20, 30))
            ax = plt.axes()
            ax.plot(time_list, vel_list)
            plt.xticks(np.arange(0, max(time_list) + 0.5, 0.5))
            plt.yticks(np.arange(0, max(vel_list) + 0.5, 1))
            plt.xlim(0, max(time_list))
            plt.ylim(0, max(vel_list))
            plt.xlabel('Time')
            plt.ylabel('Velocity of Block')
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()

            canvas.get_tk_widget().pack()

    # Instantiate the app and run it
    app = GraphsApp()
    app.mainloop()
