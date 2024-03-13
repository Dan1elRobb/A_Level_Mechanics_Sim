import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math


def projectiles_graphs():
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
        t = 0
        time_list = []
        y_dis_list = []
        x_dis_list = []
        y_vel_list = []
        while t < end_time:
            y_s = initial_vel * math.sin(math.radians(angle)) * t - 4.9 * t ** 2 + initial_height
            x_s = initial_vel * math.cos(math.radians(angle)) * t
            y_vel = initial_vel * math.sin(math.radians(angle)) - 9.8 * t
            y_dis_list.append(abs(y_s))
            x_dis_list.append(x_s)
            y_vel_list.append(y_vel)
            time_list.append(t)
            t += 0.01
        return time_list, y_dis_list, x_dis_list, y_vel_list

    def find_index_of_second_zero_displacement(dis_list):
        a = [i for i, n in enumerate(dis_list) if n < 10]
        return a[1]

    with open('PVars.txt', "r") as file:
        # Read each line and assign values to variables
        angle = float(file.readline().strip())
        mass = float(file.readline().strip())
        initial_vel = float(file.readline().strip())
        starting_height = float(file.readline().strip())
        end_time = float(file.readline().strip())

    list_of_variables = calc_variables_over_time(angle, end_time, initial_vel, starting_height)

    class GraphsApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Projectile Motion Graphs')

            y_dis_graph_page = YDisplacementTimeGraphFrame(self, "Height vs Time")
            x_dis_graph_page = XDisplacementTimeGraphFrame(self, "Horizontal Displacement vs Time")
            y_vel_graph_page = YVelocityTimeGraphFrame(self, "Y Velocity vs Time")

            y_dis_graph_page.pack(side=tk.TOP, pady=10)
            x_dis_graph_page.pack(side=tk.LEFT, padx=10)
            y_vel_graph_page.pack(side=tk.RIGHT, padx=10)

    class YDisplacementTimeGraphFrame(tk.Frame):
        def __init__(self, master, title):
            super().__init__(master)
            self.title = title
            self.create_graph()

        def create_graph(self):
            fig = plt.figure(figsize=(8, 4))
            ax = plt.axes()
            try:
                ax.plot(list_of_variables[0][:find_index_of_second_zero_displacement(list_of_variables[1]) + 10],
                        list_of_variables[1][:find_index_of_second_zero_displacement(list_of_variables[1]) + 10])
                plt.xticks(np.arange(0, max(list_of_variables[0][:find_index_of_second_zero_displacement(
                    list_of_variables[1])]) + 0.5, 0.5))
                plt.yticks(np.arange(0, max(list_of_variables[1][:find_index_of_second_zero_displacement(
                    list_of_variables[1])]) + 0.5, 2.5))
            except IndexError:
                ax.plot(list_of_variables[0],
                        list_of_variables[1])
                plt.xticks(np.arange(0, max(list_of_variables[0])))
                plt.yticks(np.arange(0, max(list_of_variables[1])))

            try:
                plt.xlim(0, max(list_of_variables[0][
                                :find_index_of_second_zero_displacement(list_of_variables[1]) + 10]))
                plt.ylim(0, max(list_of_variables[1][
                                :find_index_of_second_zero_displacement(list_of_variables[1]) + 10]))
            except IndexError:
                plt.xlim(0,max(list_of_variables[0]))
                plt.ylim(0,max(list_of_variables[1]))
            plt.grid()
            plt.title(self.title)
            ax.axhline()
            ax.axvline()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()

    class YVelocityTimeGraphFrame(tk.Frame):
        def __init__(self, master, title):
            super().__init__(master)
            self.title = title
            self.create_graph()

        def create_graph(self):
            fig = plt.figure(figsize=(8, 4))
            ax = plt.axes()
            ax.plot(list_of_variables[0], list_of_variables[3])
            plt.xticks(np.arange(0, max(list_of_variables[0]) + 0.5, 0.5))
            plt.yticks(
                np.arange(min(list_of_variables[3]), max(list_of_variables[3]),
                          5))
            plt.xlim(0, max(list_of_variables[0]))
            plt.ylim(min(list_of_variables[3]), max(list_of_variables[3]))
            plt.grid()
            plt.title(self.title)
            ax.axhline().set_color('black')
            ax.axvline()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()

    class XDisplacementTimeGraphFrame(tk.Frame):
        def __init__(self, master, title):
            super().__init__(master)
            self.title = title
            self.create_graph()

        def create_graph(self):
            fig = plt.figure(figsize=(8, 4))
            ax = plt.axes()
            ax.plot(list_of_variables[0], list_of_variables[2])
            plt.xticks(np.arange(0, max(list_of_variables[0]) + 0.5, 0.5))
            plt.yticks(
                np.arange(0, max(list_of_variables[2]),
                          20))
            plt.xlim(0, max(list_of_variables[0]))
            plt.ylim(0, max(list_of_variables[2]))
            plt.grid()
            plt.title(self.title)
            ax.axhline().set_color('black')
            ax.axvline()
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()

    app = GraphsApp()
    app.mainloop()

