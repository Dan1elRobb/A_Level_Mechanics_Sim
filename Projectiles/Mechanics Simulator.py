"""
This is the main file for the mechanics simulator that will be run first it handles user question selection
and validation for inputs and will call the 'run sim or cancel' modules when particular question types
are selected by the user
"""

import tkinter as tk
from run_projectiles_sim_or_cancel import run_sim_or_cancel
from tkinter import ttk
from run_collisions_two_particles_sim_or_cancel import run_particle_collision_sim_or_cancel
from run_collisions_partcle_and_wall_or_cancel import run_wall_collision_sim_or_cancel
from run_blocks_on_slopes_or_cancel import run_bons_sim_or_cancel
import sys
from tkinter import messagebox


class WelcomeScreen(tk.Frame):
    """
    This class is used for the display of the initial screen that the user will see, giving them the choice between the
    3 question types and also an instructions page and an exit button
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    blocks_button_clicked - the function which switches the frame to the Blocks on Slopes variables input frame using
     the switch_frame_callback function when the button is clicked
    collisions_button_clicked - the function which switches the frame to the collisions question picker frame using the
     switch_frame_callback function when the button is clicked
    projectiles_button_clicked - the function which switches the frame to the Projectiles variables input frame using
     the switch_frame_callback function when the button is clicked
    exit_button_clicked - the function which exits the program when the button is clicked - is static method
    instructions_button_clicked - the function which switches the frame to the instructions frame when the button is
     clicked

    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also defines the labels and buttons needed for the GUI to function
        Parameters
        ----------
        master
        switch_frame_callback
        """
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
        """
        This function will switch the frame to the Blocks on Slopes input frame using the self.switch_frame_callback
         function
        """
        self.switch_frame_callback(BlocksOnSlopesInputs)

    def collisions_button_clicked(self):
        """
        This function will switch the frame to the collisions question picker frame using the self.switch_frame_callback
         function
        """
        self.switch_frame_callback(CollisionQuestionSelector)

    def projectiles_button_clicked(self):
        """
        This function will switch the frame to the Projectiles input frame using the self.switch_frame_callback function
        """
        self.switch_frame_callback(ProjInputWindow)

    @staticmethod
    def exit_button_clicked():
        """
        This function will open a messagebox from tkinter which will allow user to exit the program
        """
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
        if result == 'yes':
            sys.exit()

    def instructions_button_clicked(self):
        """
        This function will switch the frame to the instructions frame using the self.switch_frame_callback function
        """
        self.switch_frame_callback(HowToUse)


class HowToUse(tk.Frame):
    """
    This class is used for the display of the GUI that explains to the user how to use the mechanics simulator
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    back_to_questions_button_clicked - will use the switch_frame_callback function to change the frame back to the
     Welcome Screen frame
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also defines the labels and buttons needed for the GUI to function
        Parameters
        ----------
        master
        switch_frame_callback
        """
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        instructions_label = ttk.Label(self, text='Welcome to my mechanics simulator.\n To use select your desired '
                                                  'question type and enter the associated variables (End time means the'
                                                  ' duration of the simulation)\n Once satisfied with your variables '
                                                  'simply press OK then the run sim button on the following window.\n '
                                                  'Press the spacebar to pause the simulation at any time.\n Once the '
                                                  'simulation has expired a pop up window will appear asking you if you'
                                                  ' would like to see graphs.\nSelect the Graphs button to get the '
                                                  'relevant graphs for the problem chosen.\n  In the same window you '
                                                  'can select "Show Variables Over Time" to see the variables '
                                                  'associated with the question type change over time\n Remember! '
                                                  'Throughout all the simulations 1 pixel is equivalent to 1m in real '
                                                  'life\n In the projectiles simulation the number in the middle of '
                                                  'the screen indicates the height of the window to give you a sense '
                                                  'of scale with the height of the projectile. \n Enjoy :D',
                                       font=('Calibri', 10))
        instructions_label.pack()

        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Question Selector',
                                      command=self.back_to_questions_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_questions_button_clicked(self):
        """
        This is the function uses by the 'Back to Question Selector' button to switch the frame to the Question Selector
        frame using te self.switch_frame_callback function to do so
        """
        self.switch_frame_callback(WelcomeScreen)


class CollisionQuestionSelector(tk.Frame):
    """
    This class is used for the display of the GUI that allows the user to pick which collisions question they would
    like simulated
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    particles_button_clicked - will use the switch_frame_callback function to switch the frame to the collisions two
     particles input frame
    wall_button_clicked - will use the switch_frame_callback function to switch the frame to the collisions particle and
     wall input frame
    back_button - will use the switch_frame_callback function to switch the frame back to the question
     selector frame

    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also defines the labels and buttons needed for the GUI to function
        Parameters
        ----------
        master
        switch_frame_callback
        """
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
        """
        This function uses the self.switch_frame_callback function to switch the frame to the collisions two particles
         input frame
        """
        self.switch_frame_callback(CollisionsTwoParticlesInputs)

    def wall_button_clicked(self):
        """
        This function uses the self.switch_frame_callback function to switch the frame to the collisions particle and
        walls input frame
        """
        self.switch_frame_callback(CollisionsParticleAndWallInputs)

    def back_button(self):
        """
        This function uses the self.switch_frame_callback function to switch the frame back to the question
         selector frame
        """
        self.switch_frame_callback(WelcomeScreen)


class ProjInputWindow(tk.Frame):
    """
    This class is used for the display of the GUI that allows the user to input the variables for the projectiles
     question type. Also validates the user inputs
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    ok_button_clicked - writes the inputted variables to the 'PVars.txt' text file to store them for use in simulation
     and graph drawing
    back_button_clicked - uses the switch_frame_callback function to switch the frame back to the question selector
     frame
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the variable input boxes for the user and assigns them default values
        Parameters
        ----------
        master
        switch_frame_callback
        """
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
        """
        This function will write the inputted user variables to the 'PVars.txt' text file but before doing so will
         validate all the inputted variables to ensure no errors occur in simulation
        """
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.angle_var.get(),
            self.mass_var.get(),
            self.initial_velocity_var.get(),
            self.starting_height_var.get(),
            self.end_time_var.get()
        ]
        # Validation of inputted variables
        global projectiles_mass_valid
        global projectiles_initial_vel_valid
        global projectiles_angle_valid
        global projectiles_end_time_valid
        global projectiles_starting_height_valid
        if int(self.angle_var.get()) <= 0:
            projectiles_angle_valid = False
        if int(self.mass_var.get()) <= 0:
            projectiles_mass_valid = False
        if int(self.initial_velocity_var.get()) <= 0:
            projectiles_initial_vel_valid = False
        if int(self.starting_height_var.get()) < 0:
            projectiles_starting_height_valid = False
        if int(self.end_time_var.get()) <= 0:
            projectiles_end_time_valid = False

        if projectiles_angle_valid and projectiles_mass_valid and projectiles_initial_vel_valid and projectiles_end_time_valid and projectiles_starting_height_valid:
            with open('PVars.txt', "w") as file:
                # Iterate over the values and write each one to a new line in the file
                for value in variables_list:
                    file.write(str(value) + "\n")
            run_sim_or_cancel()
        else:
            self.switch_frame_callback(ProjectilesInvalidVariables)

    def back_button_click(self):
        """
        This function uses the self.switch_frame_callback functino to switch the frame back to the Welcome Screen frame
        """
        self.switch_frame_callback(WelcomeScreen)


class CollisionsTwoParticlesInputs(tk.Frame):
    """
    This class is used for the display of the GUI that allows the user to input the variables for the collisions two
     particles question type. Also validates the user inputs
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    ok_button_clicked - writes the inputted variables to the 'CTPvars.txt' text file to store them for use in simulation
     and graph drawing
    back_button_clicked - uses the switch_frame_callback function to switch the frame back to the collisions question
     selector frame
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the variable input boxes for the user and assigns them default values
        Parameters
        ----------
        master
        switch_frame_callback
        """
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        # Default values
        self.mass_particle1_var = tk.DoubleVar(value=5.0)
        self.mass_particle2_var = tk.DoubleVar(value=1.0)
        self.velocity_particle1_var = tk.DoubleVar(value=10)
        self.velocity_particle2_var = tk.DoubleVar(value=5)
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
        """
        This function will write the inputted user variables to the 'CTPVars.txt' text file but before doing so will
         validate all the inputted variables to ensure no errors occur in simulation
        """
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle1_var.get(),
            self.mass_particle2_var.get(),
            self.velocity_particle1_var.get(),
            self.velocity_particle2_var.get(),
            self.coefficient_of_restitution_var.get(),
            self.end_time_var.get()
        ]
        # Validation for user inputted variables
        global ctp_mass1_valid
        global ctp_mass2_valid
        global ctp_coefficient_of_restitution_valid
        global ctp_end_time_valid
        if self.mass_particle1_var.get() <= 0:
            ctp_mass1_valid = False
        if self.mass_particle2_var.get() <= 0:
            ctp_mass2_valid = False
        if self.coefficient_of_restitution_var.get() > 1 or self.coefficient_of_restitution_var.get() < 0:
            ctp_coefficient_of_restitution_valid = False
        if self.end_time_var.get() <= 0:
            ctp_end_time_valid = False
        # Only write to text file if variables are valid
        if ctp_mass1_valid and ctp_mass2_valid and ctp_coefficient_of_restitution_valid and ctp_end_time_valid:
            with open('CTPVars.txt', "w") as file:
                # Iterate over the values and write each one to a new line in the file
                for value in variables_list:
                    file.write(str(value) + "\n")

            run_particle_collision_sim_or_cancel()
        else:
            self.switch_frame_callback(CTPInvalidVariables)

    def back_button_click(self):
        """
        This function uses the self.switch_frame_callback functino to switch the frame back to the Collision question
         picker frame
        """
        self.switch_frame_callback(CollisionQuestionSelector)


class CollisionsParticleAndWallInputs(tk.Frame):
    """
    This class is used for the display of the GUI that allows the user to input the variables for the collisions
     particle and walls question type. Also validates the user inputs
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    ok_button_clicked - writes the inputted variables to the 'CTPvars.txt' text file to store them for use in simulation
     and graph drawing
    back_button_clicked - uses the switch_frame_callback function to switch the frame back to the collisions question
     selector frame
    """

    def __init__(self, master, switch_frame_callback):
        """
       This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
       method in the class. Also creates the variable input boxes for the user and assigns them default values
       Parameters
       ----------
       master
       switch_frame_callback
       """
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
        """
        This function will write the inputted user variables to the 'CWPVars.txt' text file but before doing so will
         validate all the inputted variables to ensure no errors occur in simulation
        """
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle_var.get(),
            self.velocity_particle_var.get(),
            self.coefficient_of_restitution_var.get(),
            self.end_time_var.get()
        ]
        # Validation of user inputted variables
        global cwp_mass_valid
        global cwp_end_time_valid
        global cwp_coefficient_of_restitution_valid
        if self.mass_particle_var.get() <= 0:
            cwp_mass_valid = False
        if self.coefficient_of_restitution_var.get() > 1 or self.coefficient_of_restitution_var.get() < 0:
            cwp_coefficient_of_restitution_valid = False
        if self.end_time_var.get() <= 0:
            cwp_end_time_valid = False

        # Only write values if they are all valid
        if cwp_coefficient_of_restitution_valid and cwp_end_time_valid and cwp_mass_valid:
            with open('CWPVars.txt', "w") as file:
                # Iterate over the values and write each one to a new line in the file
                for value in variables_list:
                    file.write(str(value) + "\n")
            run_wall_collision_sim_or_cancel()
        else:
            self.switch_frame_callback(CWPInvalidVariables)

    def back_button_click(self):
        """
        This function uses the self.switch_frame_callback functino to switch the frame back to the Collision question
         picker frame
        """
        self.switch_frame_callback(CollisionQuestionSelector)


class BlocksOnSlopesInputs(tk.Frame):
    """
    This class is used for the display of the GUI that allows the user to input the variables for the blocks on slopes
     question type. Also validates the user inputs
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    ok_button_clicked - writes the inputted variables to the 'BOSvars.txt' text file to store them for use in simulation
     and graph drawing
    back_button_clicked - uses the switch_frame_callback function to switch the frame back to the collisions question
     selector frame
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the variable input boxes for the user and assigns them default values
        Parameters
        ----------
        master
        switch_frame_callback
        """
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
        """
        This function will write the inputted user variables to the 'BOSvars.txt' text file but before doing so will
         validate all the inputted variables to ensure no errors occur in simulation
        """
        # Get the values from entry widgets and store in a list
        variables_list = [
            self.mass_particle_var.get(),
            self.angle_var.get(),
            self.coefficient_of_friction_var.get(),
            self.end_time_var.get()
        ]
        # Validation of user inputted variables
        global bos_mass_valid
        global bos_angle_valid
        global bos_mew_valid
        global bos_end_time_valid
        if self.mass_particle_var.get() <= 0:
            bos_mass_valid = False
        if self.angle_var.get() <= 0:
            bos_angle_valid = False
        if self.coefficient_of_friction_var.get() < 0 or self.coefficient_of_friction_var.get() > 1:
            bos_mew_valid = False
        if self.end_time_var.get() <= 0:
            bos_end_time_valid = False
        # Only write to file if all variables are valid
        if bos_mass_valid and bos_angle_valid and bos_mew_valid and bos_end_time_valid:
            with open('BOSVars.txt', "w") as file:
                # Iterate over the values and write each one to a new line in the file
                for value in variables_list:
                    file.write(str(value) + "\n")
            run_bons_sim_or_cancel()
        else:
            self.switch_frame_callback(BOSInvalidVariables)

    def back_button_click(self):
        """
        This function uses the self.switch_frame_callback functino to switch the frame back to the Collision question
         picker frame
        """
        self.switch_frame_callback(WelcomeScreen)


# Define validity for variables globally so can be transferred between classes easily
projectiles_mass_valid = True
projectiles_angle_valid = True
projectiles_end_time_valid = True
projectiles_starting_height_valid = True
projectiles_initial_vel_valid = True


class ProjectilesInvalidVariables(tk.Frame):
    """
    This class is used for the display of the screen that informs the user that at least one of the variables inputted
     for the projectiles question type was not valid. The class also uses logic to inform the user which variable(s)
     were not valid
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    back_to_inputs_button_clicked - uses the switch_frame_callback function to switch the frame back to the projectiles
     input frame
    reset_mass_validity - resets the global projectiles_mass_valid variable so when the user re-inputs a valid variable
     the program has no issue
    reset_angle_validity - resets the global projectiles_angle_valid variable so when the user re-inputs a valid
     variable the program has no issue
    reset_initial_vel_validity - resets the global projectiles_initial_vel_valid variable so when the user re-inputs a
     valid variable the program has no issue
    reset_end_time_validity - resets the global projectiles_end_time_valid variable so when the user re-inputs a valid
     variable the program has no issue
    reset_starting_height_validity - resets the global projectiles_starting_height_valid variable so when the user
     re-inputs a valid variable the program has no issue
    All 'reset validity' methods are static
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the labels which inform the user which variable(s) were not valid. Will only
        pack the label to the frame if the variable associated with the label was not valid
        Parameters
        ----------
        master
        switch_frame_callback
        """
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        mass_invalid_label = ttk.Label(self, text='Entered Mass Is Invalid', font=('Calibri', 10))
        starting_height_invalid_label = ttk.Label(self, text='Entered Starting Height Is Invalid', font=('Calibri', 10))
        angle_invalid_label = ttk.Label(self, text='Entered Angle Is Invalid', font=('Calibri', 10))
        initial_vel_invalid_label = ttk.Label(self, text='Entered Initial Velocity Is Invalid', font=('Calibri', 10))
        end_time_invalid_label = ttk.Label(self, text='Entered End Time Is Invalid', font=('Calibri', 10))

        # Only display the 'Invalid' label if the variable was actually invalid
        if not projectiles_mass_valid:
            mass_invalid_label.pack()
            self.reset_mass_validity()
        if not projectiles_starting_height_valid:
            starting_height_invalid_label.pack()
            self.reset_starting_height_validity()
        if not projectiles_angle_valid:
            angle_invalid_label.pack()
            self.reset_angle_validity()
        if not projectiles_initial_vel_valid:
            initial_vel_invalid_label.pack()
            self.reset_initial_vel_validity()
        if not projectiles_end_time_valid:
            end_time_invalid_label.pack()
            self.reset_end_time_validity()

        # Back button
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Variable Inputs',
                                      command=self.back_to_inputs_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_inputs_button_clicked(self):
        """
        This function uses the self.switch_frame_callback function to switch the frame back to the projectiles input
         frame
        """
        self.switch_frame_callback(ProjInputWindow)

    @staticmethod
    def reset_mass_validity():
        """
        This method resets the global projectiles_mass_valid variable to True
        """
        global projectiles_mass_valid
        projectiles_mass_valid = True

    @staticmethod
    def reset_angle_validity():
        """
        This method resets the global projectiles_angle_valid variable to True
        """
        global projectiles_angle_valid
        projectiles_angle_valid = True

    @staticmethod
    def reset_initial_vel_validity():
        """
        This method resets the global projectiles_initial_vel_valid variable to True
        """
        global projectiles_initial_vel_valid
        projectiles_initial_vel_valid = True

    @staticmethod
    def reset_end_time_validity():
        """
        This method resets the global projectiles_end_time_valid variable to True
        """
        global projectiles_end_time_valid
        projectiles_end_time_valid = True

    @staticmethod
    def reset_starting_height_validity():
        """
        This method resets the global projectiles_starting_height_valid variable to True
        """
        global projectiles_starting_height_valid
        projectiles_starting_height_valid = True


# Define validity for variables globally so can be transferred between classes easily
ctp_mass1_valid = True
ctp_mass2_valid = True
ctp_coefficient_of_restitution_valid = True
ctp_end_time_valid = True


class CTPInvalidVariables(tk.Frame):
    """
    This class is used for the display of the screen that informs the user that at least one of the variables inputted
     for the collisions 2 particles question type was not valid. The class also uses logic to inform the user which
     variable(s) were not valid.
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without opening
    a new window)

    Methods
    -------
    back_to_inputs_button_clicked - uses the switch_frame_callback function to switch the frame back to the collisions
     2 particles input frame
    reset_mass1_validity - resets the global ctp_mass1_valid variable so when the user re-inputs a valid variable
     the program has no issue
    reset_mass2_validity - resets the global ctp_mass2_valid variable so when the user re-inputs a valid
     variable the program has no issue
    reset_coefficient_of_restitution_validity - resets the global ctp_coefficient_of_restitution_valid variable so when
     the user re-inputs a valid variable the program has no issue
    reset_end_time_validity - resets the global ctp_end_time_valid variable so when the user re-inputs a valid
     variable the program has no issue
    All 'reset validity' methods are static
    """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the labels which inform the user which variable(s) were not valid. Will only
        pack the label to the frame if the variable associated with the label was not valid
        Parameters
        ----------
        master
        switch_frame_callback
        """
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        mass1_invalid_label = ttk.Label(self, text='Entered Mass For Particle 1 Is Invalid', font=('Calibri', 10))
        mass2_invalid_label = ttk.Label(self, text='Entered Mass For Particle 2 Is Invalid', font=('Calibri', 10))
        coefficient_of_restitution_invalid_label = ttk.Label(self, text='Entered Coefficient Of Restitution Is Invalid',
                                                             font=('Calibri', 10))
        end_time_invalid_label = ttk.Label(self, text='Entered End Time Is Invalid', font=('Calibri', 10))
        if not ctp_mass1_valid:
            mass1_invalid_label.pack()
            self.reset_mass1_validity()
        if not ctp_mass2_valid:
            mass2_invalid_label.pack()
            self.reset_mass2_validity()
        if not ctp_coefficient_of_restitution_valid:
            coefficient_of_restitution_invalid_label.pack()
            self.reset_coefficient_of_restitution_validity()
        if not ctp_end_time_valid:
            end_time_invalid_label.pack()
            self.reset_end_time_validity()
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Variable Inputs',
                                      command=self.back_to_inputs_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_inputs_button_clicked(self):
        """
        This function uses the self.switch_frame_callback function to switch the frame back to the collisions two
         particles input frame
        """
        self.switch_frame_callback(CollisionsTwoParticlesInputs)

    @staticmethod
    def reset_mass1_validity():
        """
        This method resets the global ctp_mass1_valid variable to True
        """
        global ctp_mass1_valid
        ctp_mass1_valid = True

    @staticmethod
    def reset_mass2_validity():
        """
        This method resets the global ctp_mass2_valid variable to True
        """
        global ctp_mass2_valid
        ctp_mass2_valid = True

    @staticmethod
    def reset_end_time_validity():
        """
        This method resets the global ctp_end_time_valid variable to True
        """
        global ctp_end_time_valid
        ctp_end_time_valid = True

    @staticmethod
    def reset_coefficient_of_restitution_validity():
        """
        This method resets the global ctp_coefficient_of_restitution_valid variable to True
        """
        global ctp_coefficient_of_restitution_valid
        ctp_coefficient_of_restitution_valid = True


# Define validity for variables globally so can be transferred between classes easily
cwp_mass_valid = True
cwp_coefficient_of_restitution_valid = True
cwp_end_time_valid = True


class CWPInvalidVariables(tk.Frame):
    """
        This class is used for the display of the screen that informs the user that at least one of the variables
         inputted for the collisions particle and wall question type was not valid. The class also uses logic to inform
          the user which variable(s) were not valid.
        Attributes
        ----------
        master - the master frame/window of this class which will be the main application in all cases for now
        switch_frame_callback - a callback function which allows the program to switch to a different frame (without
        opening a new window)
        Methods
        -------
        back_to_inputs_button_clicked - uses the switch_frame_callback function to switch the frame back to the
         collisions particle and wall input frame
        reset_mass_validity - resets the global cwp_mass_valid variable so when the user re-inputs a valid variable
         the program has no issue
        reset_coefficient_of_restitution_validity - resets the global cwp_coefficient_of_restitution_valid variable so
         when the user re-inputs a valid variable the program has no issue
        reset_end_time_validity - resets the global cwp_end_time_valid variable so when the user re-inputs a valid
         variable the program has no issue
        All 'reset validity' methods are static
        """

    def __init__(self, master, switch_frame_callback):
        """
        This method uses the super() call to inherit from the tk.Frame super class and defines the switch_frame_callback
        method in the class. Also creates the labels which inform the user which variable(s) were not valid. Will only
        pack the label to the frame if the variable associated with the label was not valid
        Parameters
        ----------
        master
        switch_frame_callback
        """
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        mass_invalid_label = ttk.Label(self, text='Entered Mass For Particle Is Invalid', font=('Calibri', 10))
        coefficient_of_restitution_invalid_label = ttk.Label(self, text='Entered Coefficient Of Restitution Is Invalid',
                                                             font=('Calibri', 10))
        end_time_invalid_label = ttk.Label(self, text='Entered End Time Is Invalid', font=('Calibri', 10))
        # Only pack variables if they are valid
        if not cwp_mass_valid:
            mass_invalid_label.pack()
            self.reset_mass_validity()
        if not cwp_coefficient_of_restitution_valid:
            coefficient_of_restitution_invalid_label.pack()
            self.reset_coefficient_of_restitution_validity()
        if not cwp_end_time_valid:
            end_time_invalid_label.pack()
            self.reset_end_time_validity()

        # Back button
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Variable Inputs',
                                      command=self.back_to_inputs_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_inputs_button_clicked(self):
        """
        This method uses the self.switch_frame_callback function to switch the frame back to the collisions particle
         and wall input frame
        """
        self.switch_frame_callback(CollisionsParticleAndWallInputs)

    @staticmethod
    def reset_mass_validity():
        """
        This method resets the value of the global cwp_mass_valid variable to True
        """
        global cwp_mass_valid
        cwp_mass_valid = True

    @staticmethod
    def reset_end_time_validity():
        """
        This method resets the value of the global cwp_end_time_valid variable to True
        """
        global cwp_end_time_valid
        cwp_end_time_valid = True

    @staticmethod
    def reset_coefficient_of_restitution_validity():
        """
        This method resets the value of the global cwp_coefficient_of_restitution_valid variable to True
        """
        global cwp_coefficient_of_restitution_valid
        cwp_coefficient_of_restitution_valid = True


# Define validity for variables globally so can be transferred between classes easily
bos_mass_valid = True
bos_angle_valid = True
bos_mew_valid = True
bos_end_time_valid = True


class BOSInvalidVariables(tk.Frame):
    """
    This class is used for the display of the screen that informs the user that at least one of the variables
     inputted for the blocks on slopes question type was not valid. The class also uses logic to inform
      the user which variable(s) were not valid.
    Attributes
    ----------
    master - the master frame/window of this class which will be the main application in all cases for now
    switch_frame_callback - a callback function which allows the program to switch to a different frame (without
    opening a new window)
    Methods
    -------
    back_to_inputs_button_clicked - uses the switch_frame_callback function to switch the frame back to the
     collisions particle and wall input frame
    reset_mass_validity - resets the global bos_mass_valid variable so when the user re-inputs a valid variable
     the program has no issue
    reset_mew_validity - resets the global bos_mew_valid variable so when
     the user re-inputs a valid variable the program has no issue
    reset_end_time_validity - resets the global bos_end_time_valid variable so when the user re-inputs a valid
     variable the program has no issue
    All 'reset validity' methods are static
    """
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback

        mass_invalid_label = ttk.Label(self, text='Entered Mass Is Invalid', font=('Calibri', 10))
        angle_invalid_label = ttk.Label(self, text='Entered Angle Is Invalid', font=('Calibri', 10))
        coefficient_of_friction_invalid_label = ttk.Label(self, text='Entered Coefficient Of Friction Is Invalid',
                                                          font=('Calibri', 10))
        end_time_invalid_label = ttk.Label(self, text='Entered End Time Is Invalid', font=('Calibri', 10))
        # Only pack values to frame if they are valid
        if not bos_mass_valid:
            mass_invalid_label.pack()
            self.reset_mass_validity()
        if not bos_mew_valid:
            coefficient_of_friction_invalid_label.pack()
            self.reset_mew_validity()
        if not bos_angle_valid:
            angle_invalid_label.pack()
            self.reset_angle_validity()
        if not bos_end_time_valid:
            end_time_invalid_label.pack()
            self.reset_end_time_validity()

        # Back button
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack()

        particles_button = ttk.Button(button_frame, text='Back to Variable Inputs',
                                      command=self.back_to_inputs_button_clicked)
        particles_button.grid(row=0, column=0, padx=10, pady=10)

    def back_to_inputs_button_clicked(self):
        """
        This method uses the self.switch_frame_callback function to switch back to the blocks on slopes input frame
        """
        self.switch_frame_callback(BlocksOnSlopesInputs)

    @staticmethod
    def reset_mass_validity():
        """
        This method resets the value of the global bos_mass_valid variable to True
        """
        global bos_mass_valid
        bos_mass_valid = True

    @staticmethod
    def reset_angle_validity():
        """
        This method resets the value of the global bos_angle_valid variable to True
        """
        global bos_angle_valid
        bos_angle_valid = True

    @staticmethod
    def reset_mew_validity():
        """
        This method resets the value of the global bos_mew_valid variable to True
        """
        global bos_mew_valid
        bos_mew_valid = True

    @staticmethod
    def reset_end_time_validity():
        """
        This method resets the value of the global bos_end_time_valid variable to True
        """
        global bos_end_time_valid
        bos_end_time_valid = True


class MainApplication(tk.Tk):
    """
    This class is used to display all the frames described in classes in this module and is in charge of accurately
     swapping between them
    Methods
    -------
    switch_frame - Allows the master application to switch between different frames
    """
    def __init__(self):
        super().__init__()
        self.title("Dans Mechanics Sim")
        self.geometry("1000x300")

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
