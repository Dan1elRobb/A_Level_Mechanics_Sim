"""
This module is used to display the graphs associated with the Collisions Particles and Wall question type
"""
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk


def cwp_graphs():
    """
    This function is used so this graphs module can be run from another module with ease
    """
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('CWPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())

    # Create lists of variables
    times_list = []
    ct = 0
    particle_vel_list = []
    for _ in range(100 * int(user_end_time)):
        times_list.append(ct)
        ct += 0.1
    with open('CWP_vels.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        if float(l) != 0:
            particle_vel_list.append(float(l.strip()))

    class GraphsApp(tk.Tk):
        """
        This class is responsible for the main window of the graphs display - all graphs that will be displayed
        (currently only one) can be stuck on to this window
        """
        def __init__(self):
            super().__init__()
            self.title('Collision wall and particle graphs')

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
            ax.plot(times_list[:len(particle_vel_list)], particle_vel_list)
            plt.xlim(0, max(times_list))
            plt.ylim(min(particle_vel_list) - 10, max(particle_vel_list) + 10)
            ax.axhline()
            ax.axvline()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            plt.xlabel('Time')
            plt.ylabel('Velocity')

            canvas.get_tk_widget().pack()
    # Instantiate the app and run the main loop
    app = GraphsApp()
    app.mainloop()
