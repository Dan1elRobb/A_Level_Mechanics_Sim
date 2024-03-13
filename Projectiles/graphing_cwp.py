import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math

def cwp_graphs():
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('CWPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())

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
        def __init__(self):
            super().__init__()
            self.title('Collision wall and particle graphs')

            y_vel_graph_page = VelocityTimeGraphFrame(self, "Velocity vs Time")

            y_vel_graph_page.pack(padx=10)

    class VelocityTimeGraphFrame(tk.Frame):
        def __init__(self, master, title):
            super().__init__(master)
            self.title = title
            self.create_graph()
        def create_graph(self):
            fig = plt.figure(figsize=(20, 30))
            ax = plt.axes()
            ax.plot(times_list[:len(particle_vel_list)], particle_vel_list)
            plt.xlim(0,max(times_list))
            plt.ylim(min(particle_vel_list)-10,max(particle_vel_list)+10)
            ax.axhline()
            ax.axvline()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            plt.xlabel('Time')
            plt.ylabel('Velocity')

            canvas.get_tk_widget().pack()
    app = GraphsApp()
    app.mainloop()
