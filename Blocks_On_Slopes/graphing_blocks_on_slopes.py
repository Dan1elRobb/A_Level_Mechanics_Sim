import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from BlockOnSlopeCalcSuite import calc_v_over_time


class VelocityTimeGraphFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        fig = plt.figure(figsize=(20, 30))
        ax = plt.axes()
        ax.plot(calc_v_over_time(60, 0.5, 10)[1], calc_v_over_time(60, 0.5, 10)[0])
        plt.xticks(np.arange(0, max(calc_v_over_time(60, 0.5, 10)[1]) + 0.5, 0.5))
        plt.yticks(np.arange(0, max(calc_v_over_time(60, 0.5, 10)[0]) + 0.5, 0.5))
        plt.xlim(0, 10)
        plt.ylim(0, max(calc_v_over_time(60, 0.5, 10)[0]))

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.get_tk_widget().pack()


root = tk.Tk()
root.title('Velocity time graph')
graph_page = VelocityTimeGraphFrame()
graph_page.pack()
root.mainloop()

