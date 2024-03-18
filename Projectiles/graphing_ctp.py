"""
This module is used to display the graphs associated with the Collisions Two Particles question type
"""

import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk


def ctp_graphs():
    """
    This function is used so this graphs module can be run from another module with ease
    """
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('CTPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())

    # Create lists of variables
    times_list = []
    ct = 0
    particle1_vel_list = []
    particle2_vel_list = []
    for _ in range(100 * int(user_end_time)):
        times_list.append(ct)
        ct += 0.01
    with open('CTP1_vels.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        particle1_vel_list.append(float(l.strip()))
    with open('CTP2_vels.txt', 'r') as f:
        lin = f.readlines()
    for l in lin:
        particle2_vel_list.append(float(l.strip()))
    # Find lowest and highest values in both velocities lists - for the sake of graphs showing correct ranges
    min_particle1_vels = min(particle1_vel_list)
    max_particle1_vels = max(particle1_vel_list)
    min_particle2_vels = min(particle2_vel_list)
    max_particle2_vels = max(particle2_vel_list)

    class GraphsApp(tk.Tk):
        """
        This class is responsible for the main window of the graphs display - all graphs that will be displayed
        (currently only one) can be stuck on to this window
        """
        def __init__(self):
            super().__init__()
            self.title('Collisions 2 particles graphs')

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
            # Avoid indexing errors by truncating lists
            try:
                ax.plot(times_list[:min(len(particle1_vel_list)-5, len(particle2_vel_list)-5)],
                        particle1_vel_list[:min(len(particle1_vel_list), len(particle2_vel_list))], label="Particle 1")
                ax.plot(times_list[:min(len(particle1_vel_list)-5, len(particle2_vel_list)-5)],
                        particle2_vel_list[:min(len(particle1_vel_list)-5, len(particle2_vel_list)-5)], label="Particle 2")
            except ValueError:
                ax.plot(times_list[:250],
                        particle1_vel_list[:250], label="Particle 1")
                ax.plot(times_list[:250],
                        particle2_vel_list[:250],
                        label="Particle 2")

            plt.xlim(0, user_end_time + 5)
            plt.ylim(min(min_particle1_vels, min_particle2_vels) - 10, max(max_particle1_vels, max_particle2_vels) + 10)
            ax.axhline()
            ax.axvline()
            plt.legend()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            plt.xlabel('Time')
            plt.ylabel('Velocity')
            canvas.get_tk_widget().pack()
    # Instatiate the app and run the main loop
    app = GraphsApp()
    app.mainloop()
