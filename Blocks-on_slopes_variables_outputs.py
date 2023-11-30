from BlockOnSlopeCalcSuite import calc_a, calc_m, calc_angle, calc_f_m, calc_m_with_acc
import math
import tkinter as tk
from tkinter import ttk

m = 10


class Outputs_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Your Variables good sir')
        self.geometry('1280x720')
        self.label = ttk.Label(self, text=f'Mass: {m}')
        self.label.pack()


if __name__ == "__main__":
    gui = Outputs_GUI()
    gui.mainloop()
