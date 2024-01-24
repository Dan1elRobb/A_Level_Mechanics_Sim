import tkinter as tk
from tkinter import ttk


def run_collision_question_selector():
    class CollisionQuestionSelector(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Collision Question Selector')
            self.geometry('400x200')

            # Welcome Label
            welcome_label = ttk.Label(self, text='Select Collision Question Type', font=('Helvetica', 16))
            welcome_label.pack(pady=20)

            # Button Frame
            button_frame = ttk.Frame(self, padding=10)
            button_frame.pack()

            # Buttons
            particles_button = ttk.Button(button_frame, text='Two Particles', command=self.particles_button_clicked)
            particles_button.grid(row=0, column=0, padx=10, pady=10)

            wall_button = ttk.Button(button_frame, text='Particle and Wall', command=self.wall_button_clicked)
            wall_button.grid(row=0, column=1, padx=10, pady=10)

        def particles_button_clicked(self):
            # Placeholder for the functionality when the "Two Particles" button is clicked
            print("Two Particles button clicked")

        def wall_button_clicked(self):
            # Placeholder for the functionality when the "Particle and Wall" button is clicked
            print("Particle and Wall button clicked")

    collision_selector = CollisionQuestionSelector()
    collision_selector.mainloop()
