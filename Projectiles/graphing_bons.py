import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math
def bons_graphs():
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    with open('BOSVars.txt', "r") as file:
        # Read each line and assign values to variables
        mass = float(file.readline().strip())
        angle = float(file.readline().strip())
        mew = float(file.readline().strip())
        end_time = float(file.readline().strip())
    def calc_v_over_time(angle, mew, end_time):
        t = 0
        time_list = []
        vel_list = []
        while t < end_time:
            v = 9.8 * t * (math.sin(angle) - math.cos(angle) * mew)
            vel_list.append(v)
            time_list.append(t)
            t += 0.01
        return vel_list, time_list

    vel_list = calc_v_over_time(math.radians(angle), mew, end_time)[0]
    time_list = calc_v_over_time(math.radians(angle), mew, end_time)[1]


    class GraphsApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Blocks on slopes graphs')

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


    app = GraphsApp()
    app.mainloop()
