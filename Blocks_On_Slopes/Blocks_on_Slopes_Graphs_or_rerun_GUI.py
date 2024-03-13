import tkinter as tk
from tkinter import ttk
from Main.blocks_on_slopes_simulation import Sim
from graphing_blocks_on_slopes import VelocityTimeGraphFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Graph or ReRun')
        self.geometry('1280x720')

        self.label = ttk.Label(self, text='Graphs Or Rerun')
        self.label.pack()

        self.button = ttk.Button(self, text='Graphs')
        self.button['command'] = self.graphs_button_clicked
        self.button.pack()

        self.button = ttk.Button(self, text='ReRun Simulation')
        self.button['command'] = self.rerun_button_clicked
        self.button.pack()

    def rerun_button_clicked(self):
        Sim().run()

    def graphs_button_clicked(self):
        root = tk.Tk()
        root.title('Velocity time graph')
        graph_page = VelocityTimeGraphFrame()
        graph_page.pack()
        root.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()
