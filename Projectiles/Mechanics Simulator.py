import tkinter as tk
from run_projectiles_sim_or_cancel import run_sim_or_cancel
from tkinter import ttk
from run_collisions_two_particles_sim_or_cancel import run_particle_collision_sim_or_cancel
from run_collisions_partcle_and_wall_or_cancel import run_wall_collision_sim_or_cancel
from run_blocks_on_slopes_or_cancel import run_bons_sim_or_cancel
import sys
from tkinter import messagebox


class WelcomeScreen(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
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

        projectiles_button = ttk.Button(button_frame, text='Projectiles', command=self.projectiles_button_clicked)
        projectiles_button.grid(row=0, column=2, padx=10, pady=10)

        exit_button = ttk.Button(button_frame, text='Exit Application', command=self.exit_button_clicked)
        exit_button.grid(row=5, column=1, padx=10, pady=10)

        instructions_button = ttk.Button(button_frame, text='Instructions!', command=self.instructions_button_clicked)
        instructions_button.grid(row=4, column=1, padx=10, pady=10)

        # Custom style for the Frame to set the background color
        self.style = ttk.Style()
        self.style.configure('Button.TFrame', background='#f0f0f0')

    def blocks_button_clicked(self):
        # Placeholder for the functionality when the "Blocks on Slopes" button is clicked
        self.switch_frame_callback(BlocksOnSlopesInputs)

    def collisions_button_clicked(self):
        # Placeholder for the functionality when the "Collisions" button is clicked
        self.switch_frame_callback(CollisionQuestionSelector)

    def projectiles_button_clicked(self):
        # Placeholder for the functionality when the "Projectiles" button is clicked
        self.switch_frame_callback(ProjInputWindow)

    def exit_button_clicked(self):
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
        if result == 'yes':
            sys.exit()

    def instructions_button_clicked(self):
        self.switch_frame_callback(HowToUse)


class HowToUse(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        instructions_label = ttk.Label(self, text='Welcome to my mechanics simulator.\n To use select your desired '
                                                  'question type and enter the associated variables (End time means the'
                                                  ' duration of the simulation)\n Once satisfied with your variables '
                                                  'simply press OK then the run sim button on the following window.\n '
                                                  'Press the spacebar to pause the simulation at any time.\n Once the '
                                                  'simulation has expired a pop up window will appear asking you if you'
                                                  ' would like to see graphs.\n Select the Graphs button to get the '
                                                  'relevant graphs for the problem chosen.\n Enjoy :D',
                                       font=('Calibri', 10))
        instructions_label.pack()

        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Question Selector',
                                      command=self.back_to_questions_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_questions_button_clicked(self):
        self.switch_frame_callback(WelcomeScreen)


class CollisionQuestionSelector(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        # Welcome Label
        welcome_label = ttk.Label(self, text='Select Collision Question Type', font=('Helvetica', 16))
        welcome_label.pack()

        # Button Frame
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        # Buttons
        particles_button = ttk.Button(button_frame, text='Two Particles', command=self.particles_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

        wall_button = ttk.Button(button_frame, text='Particle and Wall', command=self.wall_button_clicked)
        wall_button.grid(row=0, column=1, padx=10, pady=10)

        back_button = ttk.Button(button_frame, text='Back', command=self.back_button)
        back_button.grid(row=0, column=2, padx=10, pady=10)

    def particles_button_clicked(self):
        # Placeholder for the functionality when the "Two Particles" button is clicked
        self.switch_frame_callback(CollisionsTwoParticlesInputs)

    def wall_button_clicked(self):
        # Placeholder for the functionality when the "Particle and Wall" button is clicked
        self.switch_frame_callback(CollisionsParticleAndWallInputs)

    def back_button(self):
        self.switch_frame_callback(WelcomeScreen)


class ProjInputWindow(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.angle_var = tk.DoubleVar(value=45.0)
        self.mass_var = tk.DoubleVar(value=1.0)
        self.initial_velocity_var = tk.DoubleVar(value=40)
        self.starting_height_var = tk.DoubleVar(value=10)
        self.end_time_var = tk.DoubleVar(value=15)

        # Labels and entry widgets
        ttk.Label(self, text="Angle (degrees):").grid(row=0, column=0, padx=10, pady=5)
        self.angle_entry = tk.Entry(self, textvariable=self.angle_var)
        self.angle_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Mass (kg):").grid(row=1, column=0, padx=10, pady=5)
        self.mass_entry = tk.Entry(self, textvariable=self.mass_var)
        self.mass_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Initial Velocity (m/s):").grid(row=2, column=0, padx=10, pady=5)
        self.initial_velocity_entry = tk.Entry(self, textvariable=self.initial_velocity_var)
        self.initial_velocity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Starting Height (m):").grid(row=3, column=0, padx=10, pady=5)
        self.starting_height_entry = tk.Entry(self, textvariable=self.starting_height_var)
        self.starting_height_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self, text="End Time (s):").grid(row=4, column=0, padx=10, pady=5)
        self.end_time_entry = tk.Entry(self, textvariable=self.end_time_var)
        self.end_time_entry.grid(row=4, column=1, padx=10, pady=5)

        # OK button
        ttk.Button(self, text="OK", command=self.ok_button_click).grid(row=5, column=0, columnspan=2, pady=10)

        # Back button
        ttk.Button(self, text='Go back', command=self.back_button_click).grid(row=6, column=0, columnspan=2, pady=10)

    def ok_button_click(self):
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.angle_var.get(),
            self.mass_var.get(),
            self.initial_velocity_var.get(),
            self.starting_height_var.get(),
            self.end_time_var.get()
        ]
        # Print the values (you can modify this part based on your use case)
        with open('PVars.txt', "w") as file:
            # Iterate over the values and write each one to a new line in the file
            for value in variables_list:
                file.write(str(value) + "\n")
        run_sim_or_cancel()

    def back_button_click(self):
        self.switch_frame_callback(WelcomeScreen)


class CollisionsTwoParticlesInputs(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.mass_particle1_var = tk.DoubleVar(value=5.0)
        self.mass_particle2_var = tk.DoubleVar(value=1.0)
        self.velocity_particle1_var = tk.DoubleVar(value=25)
        self.velocity_particle2_var = tk.DoubleVar(value=40)
        self.coefficient_of_restitution_var = tk.DoubleVar(value=0.8)
        self.end_time_var = tk.DoubleVar(value=15)

        # Labels and entry widgets using grid
        tk.Label(self, text="Mass Particle 1 (kg):").grid(row=0, column=0, padx=10, pady=5)
        self.mass_particle1_entry = tk.Entry(self, textvariable=self.mass_particle1_var)
        self.mass_particle1_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Mass Particle 2 (kg):").grid(row=1, column=0, padx=10, pady=5)
        self.mass_particle2_entry = tk.Entry(self, textvariable=self.mass_particle2_var)
        self.mass_particle2_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Velocity Particle 1 (m/s):").grid(row=2, column=0, padx=10, pady=5)
        self.velocity_particle1_entry = tk.Entry(self, textvariable=self.velocity_particle1_var)
        self.velocity_particle1_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Velocity Particle 2 (m/s):").grid(row=3, column=0, padx=10, pady=5)
        self.velocity_particle2_entry = tk.Entry(self, textvariable=self.velocity_particle2_var)
        self.velocity_particle2_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Coefficient of Restitution:").grid(row=4, column=0, padx=10, pady=5)
        self.coefficient_of_restitution_entry = tk.Entry(self, textvariable=self.coefficient_of_restitution_var)
        self.coefficient_of_restitution_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self, text="End Time (s):").grid(row=5, column=0, padx=10, pady=5)
        self.end_time_entry = tk.Entry(self, textvariable=self.end_time_var)
        self.end_time_entry.grid(row=5, column=1, padx=10, pady=5)

        # OK button
        ttk.Button(self, text="OK", command=self.ok_button_click).grid(row=6, column=0, columnspan=2, pady=10)

        # Back button
        ttk.Button(self, text='Go back', command=self.back_button_click).grid(row=7, column=0, columnspan=2,
                                                                              pady=10)

    def ok_button_click(self):
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle1_var.get(),
            self.mass_particle2_var.get(),
            self.velocity_particle1_var.get(),
            self.velocity_particle2_var.get(),
            self.coefficient_of_restitution_var.get(),
            self.end_time_var.get()
        ]
        # Print the values (you can modify this part based on your use case)
        with open('CTPVars.txt', "w") as file:
            # Iterate over the values and write each one to a new line in the file
            for value in variables_list:
                file.write(str(value) + "\n")

        run_particle_collision_sim_or_cancel()

    def back_button_click(self):
        self.switch_frame_callback(CollisionQuestionSelector)


class CollisionsParticleAndWallInputs(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.mass_particle_var = tk.DoubleVar(value=5.0)
        self.velocity_particle_var = tk.DoubleVar(value=20)
        self.coefficient_of_restitution_var = tk.DoubleVar(value=0.8)
        self.end_time_var = tk.DoubleVar(value=15)

        # Labels and entry widgets using grid
        tk.Label(self, text="Mass Particle (kg):").grid(row=0, column=0, padx=10, pady=5)
        self.mass_particle1_entry = tk.Entry(self, textvariable=self.mass_particle_var)
        self.mass_particle1_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Velocity Particle (m/s):").grid(row=1, column=0, padx=10, pady=5)
        self.velocity_particle1_entry = tk.Entry(self, textvariable=self.velocity_particle_var)
        self.velocity_particle1_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Coefficient of Restitution:").grid(row=2, column=0, padx=10, pady=5)
        self.coefficient_of_restitution_entry = tk.Entry(self, textvariable=self.coefficient_of_restitution_var)
        self.coefficient_of_restitution_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="End Time (s):").grid(row=3, column=0, padx=10, pady=5)
        self.end_time_entry = tk.Entry(self, textvariable=self.end_time_var)
        self.end_time_entry.grid(row=3, column=1, padx=10, pady=5)

        # OK button
        ttk.Button(self, text="OK", command=self.ok_button_click).grid(row=6, column=0, columnspan=2, pady=10)

        # Back button
        ttk.Button(self, text='Go back', command=self.back_button_click).grid(row=7, column=0, columnspan=2,
                                                                              pady=10)

    def ok_button_click(self):
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle_var.get(),
            self.velocity_particle_var.get(),
            self.coefficient_of_restitution_var.get(),
            self.end_time_var.get()
        ]
        # Print the values (you can modify this part based on your use case)
        with open('CWPVars.txt', "w") as file:
            # Iterate over the values and write each one to a new line in the file
            for value in variables_list:
                file.write(str(value) + "\n")
        run_wall_collision_sim_or_cancel()

    def back_button_click(self):
        self.switch_frame_callback(CollisionQuestionSelector)


class BlocksOnSlopesInputs(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.angle_var = tk.DoubleVar(value=30.0)
        self.mass_particle_var = tk.DoubleVar(value=5.0)
        self.coefficient_of_friction_var = tk.DoubleVar(value=0.3)
        self.end_time_var = tk.DoubleVar(value=15)

        # Labels and entry widgets using grid
        tk.Label(self, text="Angle of slope (degrees):").grid(row=0, column=1, padx=10, pady=5)
        self.velocity_particle1_entry = tk.Entry(self, textvariable=self.angle_var)
        self.velocity_particle1_entry.grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self, text="Mass Block (kg):").grid(row=1, column=1, padx=10, pady=5)
        self.mass_particle1_entry = tk.Entry(self, textvariable=self.mass_particle_var)
        self.mass_particle1_entry.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self, text="Coefficient of friction:").grid(row=2, column=1, padx=10, pady=5)
        self.coefficient_of_restitution_entry = tk.Entry(self, textvariable=self.coefficient_of_friction_var)
        self.coefficient_of_restitution_entry.grid(row=2, column=2, padx=10, pady=5)

        tk.Label(self, text="End Time (s):").grid(row=3, column=1, padx=10, pady=5)
        self.end_time_entry = tk.Entry(self, textvariable=self.end_time_var)
        self.end_time_entry.grid(row=3, column=2, padx=10, pady=5)

        # OK button
        ttk.Button(self, text="OK", command=self.ok_button_click).grid(row=6, column=1, columnspan=2, pady=10)

        # Back button
        ttk.Button(self, text='Go back', command=self.back_button_click).grid(row=7, column=1, columnspan=2,
                                                                              pady=10)

    def ok_button_click(self):
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle_var.get(),
            self.angle_var.get(),
            self.coefficient_of_friction_var.get(),
            self.end_time_var.get()
        ]
        # Print the values (you can modify this part based on your use case)
        with open('BOSVars.txt', "w") as file:
            # Iterate over the values and write each one to a new line in the file
            for value in variables_list:
                file.write(str(value) + "\n")
        run_bons_sim_or_cancel()

    def back_button_click(self):
        self.switch_frame_callback(WelcomeScreen)


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dans Mechanics Sim")
        self.geometry("700x300")

        self.current_frame = None
        self.switch_frame(WelcomeScreen)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.switch_frame)

        if self.current_frame:
            self.current_frame.destroy()

        new_frame.pack(fill="both", expand=True)
        self.current_frame = new_frame


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
