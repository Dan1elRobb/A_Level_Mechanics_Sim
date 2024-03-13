import tkinter as tk
from tkinter import ttk


class WelcomeScreen(tk.Tk):
    def __init__(self,master,switch_frame_callback):
        super().__init__()
        self.title('A level Mechanics Simulator')
        self.geometry('400x300')
        self.configure(bg='#f0f0f0')  # Set background color

        # Welcome Label
        welcome_label = ttk.Label(self, text='Welcome to the Mechanics simulator', font=('Helvetica', 16),
                                  background='#f0f0f0')
        welcome_label.pack(pady=20)

        # Button Frame
        button_frame = ttk.Frame(self, padding=10, style='Button.TFrame')  # Using a ttk Frame with a custom style
        button_frame.pack()

        # Buttons
        blocks_button = ttk.Button(button_frame, text='Blocks on Slopes', command=self.blocks_button_clicked)
        blocks_button.grid(row=0, column=0, padx=10, pady=10)

        collisions_button = ttk.Button(button_frame, text='Collisions', command=self.collisions_button_clicked)
        collisions_button.grid(row=0, column=1, padx=10, pady=10)

        projectiles_button = ttk.Button(button_frame, text='Main', command=self.projectiles_button_clicked)
        projectiles_button.grid(row=0, column=2, padx=10, pady=10)

        # Custom style for the Frame to set the background color
        self.style = ttk.Style()
        self.style.configure('Button.TFrame', background='#f0f0f0')

    def blocks_button_clicked(self):
        # Placeholder for the functionality when the "Blocks on Slopes" button is clicked
        print('BONS')

    def collisions_button_clicked(self):
        # Placeholder for the functionality when the "Collisions" button is clicked
        print('C')

    def projectiles_button_clicked(self):
        # Placeholder for the functionality when the "Main" button is clicked
        Projectiles_Variables_Inputs.running_inputs()


if __name__ == "__main__":
    welcome_screen = WelcomeScreen()
    welcome_screen.mainloop()
