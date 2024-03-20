'''
This module handles the GUI for the outputs over time of the projectiles question type
Does not incorporate any other written modules as it is a terminating GUI and does not lead to any
other GUIs
'''
import tkinter as tk
import math


def run_proj_outputs():
    class Projectiles_Variable_Outputs_GUI:
        """
        This class is used for the actual display of the outputs of the collision with particle and
        wall question type. It takes in 2 lists and will loop through these lists displaying each item
        inside the lists at 0.01s intervals
        Attributes
        ----------
        root - This is the root of the window and allows tkinter to display the GUI and run a main
        loop through it
        y_vel_list - This is a list of vertical component of the velocity of the particle which is generated in this
         module by the calc_variables_over_time function
        y_dis_list - This is a list of vertical displacement of the particle which is generated in this
         module by the calc_variables_over_time function
        x_dis_list - This is a list of horizontal displacement of the particle which is generated in this
         module by the calc_variables_over_time function
        time_list - This is a list of times at 0.01s intervals and is generated in this module

        Methods
        -------
        update_label - The method which updates the text labels every 0.01s as long as the index pointer is in range
        of the length of the shortest list generated
        close_gui - The method which destroys the root and thus closes the GUI - designed to mean that this module can
        be reused in the same instance of the progam, and it will start from the beginning of the lists when run each time
        """
        def __init__(self, root, y_vel_list, time_list, y_dis_list, x_dis_list):
            """
            Defines the root of the window and the lists of the variables to be displayed in the GUI
            Parameters
            ----------
            root - root of the tkinter window
            y_vel_list - list of vertical components of velocity of the particle
            time_list - list of times at 0.01s intervals
            y_dis_list - list of vertical displacement of particle
            x_dis_list - list of horizontal displacement of particle
            """
            self.root = root
            self.root.title("Blocks On Slopes Variable Outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.y_vel_list = y_vel_list
            self.time_list = time_list
            self.x_dis_list = x_dis_list
            self.y_dis_list = y_dis_list
            self.current_index = 0

            # Create labels and pack them
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.y_vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.y_vel_label.pack(pady=10)
            self.x_dis_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.x_dis_label.pack(pady=10)
            self.y_dis_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.y_dis_label.pack(pady=10)

            # Create a button to close the GUI
            self.close_button = tk.Button(root, text="Close", command=self.close_gui)
            self.close_button.pack(pady=10)

            # Call the update_label method every 10 milliseconds (0.01 second)
            self.root.after(10, self.update_label)

        def update_label(self):
            """
            This method updates the different variable labels at 0.01s intervals
            """
            # Get the current value from the list
            current_y_vel = self.y_vel_list[self.current_index]
            current_time = self.time_list[self.current_index]
            current_x_dis = self.x_dis_list[self.current_index]
            current_y_dis = self.y_dis_list[self.current_index]

            # Update the label with the current value
            y_vel_display = f' Y Velocity: {str(current_y_vel)[0:5]}'
            time_display = f'Time: {str(current_time)[0:4]}'
            x_dis_display = f'X Displacement: {str(current_x_dis)[0:6]}'
            y_dis_display = f'Height: {str(current_y_dis)[0:6]}'
            self.y_vel_label.config(text=y_vel_display)
            self.time_label.config(text=time_display)
            self.x_dis_label.config(text=x_dis_display)
            self.y_dis_label.config(text=y_dis_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            # Call the update_label method again after 10 milliseconds (0.01 seconds)
            if self.current_index < len(self.time_list) and self.current_index < len(self.y_vel_list) and self.current_index < len(self.x_dis_list) and self.current_index < len(self.y_dis_list):
                self.root.after(10, self.update_label)

        def close_gui(self):
            """
            This is the command function for the 'Close' button - destroys the root of the GUI to allow for reuse in same instance

            """
            self.root.destroy()
    # Open and read the text file containing all the variables inputted by user for projectiles question type
    with open('PVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_angle = float(file.readline().strip())
        user_mass = float(file.readline().strip())
        user_initial_vel = float(file.readline().strip())
        user_starting_height = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
        # Simulation setup
    mass = user_mass
    angle = user_angle  # Initial angle in degrees
    start_height = user_starting_height
    initial_velocity = user_initial_vel  # Adjust the initial speed as needed

    def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
        """
        This function takes in the variables provided by the user and uses kinematics equations to calculate the needed
        outputs at 0.01s intervals. Puts outputs in lists
        Parameters
        ----------
        angle - angle of projection of the particle (provided by the user)
        end_time - duration of simulation (provided by the user)
        initial_vel - initial velocity of the particle (provided by the user)
        initial_height - initial height of the particle (provided by the user)

        Returns
        -------
        List of lists - [time_list, y_dis_list, x_dis_list, y_vel_list]
        """
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
    # Use the calc_variables_over_time functino to generate the lists needed for outputs
    time_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[0]
    y_dis_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[1]
    x_dis_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[2]
    y_vel_list = calc_variables_over_time(angle, user_end_time, initial_velocity, start_height)[3]

    # Instantiate the GUI using the users inputs
    root = tk.Tk()
    app = Projectiles_Variable_Outputs_GUI(root, y_vel_list, time_list, y_dis_list, x_dis_list)
    root.mainloop()



