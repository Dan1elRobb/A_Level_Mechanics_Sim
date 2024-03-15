import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math


def ctp_graphs():
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('CTPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())

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
        def __init__(self):
            super().__init__()
            self.title('Collisions 2 particles graphs')

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
            ax.plot(times_list[:min(len(particle1_vel_list),len(particle2_vel_list))], particle1_vel_list[:min(len(particle1_vel_list),len(particle2_vel_list))], label="Particle 1")
            ax.plot(times_list[:min(len(particle1_vel_list),len(particle2_vel_list))], particle2_vel_list[:min(len(particle1_vel_list),len(particle2_vel_list))], label="Particle 2")
            plt.xlim(0, user_end_time+5)
            plt.ylim(min(min_particle1_vels,min_particle2_vels) - 10, max(max_particle1_vels,max_particle2_vels) + 10)
            ax.axhline()
            ax.axvline()
            plt.legend()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            plt.xlabel('Time')
            plt.ylabel('Velocity')
            canvas.get_tk_widget().pack()
    print(len (times_list),len(particle1_vel_list),len(particle2_vel_list))
    app = GraphsApp()
    app.mainloop()
