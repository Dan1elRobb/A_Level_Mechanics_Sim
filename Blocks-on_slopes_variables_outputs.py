from BlockOnSlopeCalcSuite import calc_a, calc_m, calc_angle, calc_f_m, calc_m_with_acc
import math
import tkinter as tk
from tkinter import ttk

class Outputs_GUI(tk.Tk):
    def __init__(self,m,a,angle,f):
        super().__init__()
        self.m = m
        self.title('Your Variables good sir')
        self.geometry('1280x720')
        self.label = ttk.Label(self, text=f'Mass: {self.m}')
        self.label.pack()
    def m_minus_one(self):
        self.m -= 1



if __name__ == "__main__":
    gui = Outputs_GUI(10,2,30,4)
    while True:
        gui.m_minus_one()
        Outputs_GUI.update(gui)
        Outputs_GUI.update_idletasks(gui)

