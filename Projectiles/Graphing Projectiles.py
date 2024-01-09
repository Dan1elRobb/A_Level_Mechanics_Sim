import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import math

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
        y_dis_list.append(y_s)
        x_dis_list.append(x_s)
        y_vel_list.append(y_vel)
        time_list.append(t)
        t += 0.01
    return time_list, y_dis_list, x_dis_list, y_vel_list


class YVelocityTimeGraphFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        fig = plt.figure(figsize=(20, 30))
        ax = plt.axes()
        ax.plot(calc_variables_over_time(30, 15, 15, 0)[0], calc_variables_over_time(30, 15, 15, 0)[1])
        plt.xticks(np.arange(0, max(calc_variables_over_time(30, 15, 15, 0)[0]) + 0.5, 0.5))
        plt.yticks(np.arange(0, max(calc_variables_over_time(30, 15, 15, 0)[1]) + 0.5, 0.5))
        plt.xlim(0, 10)
        plt.ylim(-10, max(calc_variables_over_time(30, 15, 15, 0)[1]))

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.get_tk_widget().pack()

root = tk.Tk()
root.title('Velocity time graph')
graph_page = YVelocityTimeGraphFrame()
graph_page.pack()
root.mainloop()
