'''
This module is used to display the changing velocity of the block on the slope over time
Uses a tkinter window
Does not import any other modules which I have written as it is a terminating GUI meaning
you cannot open another window or frame from this GUI
'''
import tkinter as tk
import math


def run_bons_outputs():
    """
    This function allows other modules to be able to bring up the outputs at any given point
    by importing this module and executing this function
    """

    class Blocks_on_slopes_Variable_Outputs_GUI:
        """
        This class is used for the actual display of the outputs of the Blocks on Slopes question type.
        It takes in 2 lists and will loop through these lists displaying each item inside the lists at 0.01s intervals
        Attributes
        ----------
        root - This is the root of the window and allows tkinter to display the GUI and run a main
        loop through it
        vel_list - This is a list of velocities of the block which is generated in this module by the calc_v_over_time function
        time_list - This is a list of times at 0.01s intervals and is generated in this module by the calc_v_over_time function

        Methods
        -------
        update_label - The method which updates the text labels every 0.01s as long as the index pointer is in range
        of the length of the shortest list generated
        close_gui - The method which destroys the root and thus closes the GUI - designed to mean that this module can
        be reused in the same instance of the progam, and it will start from the beginning of the lists when run each time
        """
        def __init__(self, root, vel_list, time_list):
            """
            Define the velocity and time lists which will be displayed in the GUI
            Define the root of the tkinter window
            Parameters
            ----------
            root
            vel_list
            time_list
            """
            self.root = root
            self.root.title("Blocks On Slopes Variable Outputs")
            self.root.geometry("500x400")
            # List of values to display
            self.vel_list = vel_list
            self.time_list = time_list
            self.current_index = 0

            # Create a label and pack it
            self.time_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.time_label.pack(pady=10)
            self.vel_label = tk.Label(root, text="", font=("Helvetica", 14))
            self.vel_label.pack(pady=10)

            # Create a button to close the GUI
            self.close_button = tk.Button(root, text="Close", command=self.close_gui)
            self.close_button.pack(pady=10)

            # Call the update_label method every 10 milliseconds (0.01 seconds)
            self.root.after(10, self.update_label)

        def update_label(self):
            # Get the current value from the list
            current_vel = self.vel_list[self.current_index]
            current_time = self.time_list[self.current_index]

            # Update the label with the current value
            vel_display = f'Velocity: {str(current_vel)[0:5]}'
            time_display = f'Time: {str(current_time)[0:4]}'
            self.vel_label.config(text=vel_display)
            self.time_label.config(text=time_display)

            # Move to the next value in the list
            self.current_index = self.current_index + 1

            ''' Ensure that the index do not go out of range
            before calling the update_label method again after 10 milliseconds (0.01 seconds)'''
            if self.current_index < len(self.time_list) and self.current_index < len(self.vel_list):
                self.root.after(10, self.update_label)
            else:
                pass

        def close_gui(self):
            self.root.destroy()

    def calc_v_over_time(angle, mew, end_time):
        """
        This function calculates the velocity of the block on the slope at 0.01 second intervals
        and generates a list with all of these velocities in it
        Also generates a list of times 0.01 seconds apart
        Parameters
        ----------
        angle
        mew
        end_time

        Returns
        -------
        List of velocities of the block at 0.01 second intervals
        List of times 0.01 seconds apart
        """
        t = 0
        time_list = []
        vel_list = []
        while t < end_time:
            v = 9.8 * t * (math.sin(angle) - math.cos(angle) * mew)
            vel_list.append(v)
            time_list.append(t)
            t += 0.01
        return vel_list, time_list
    # Read the text file in which the variables inputted by the user for this question type were written
    with open('BOSVars.txt', "r") as file:
        # Read each line and assign values to variables
        mass = float(file.readline().strip())
        angle = float(file.readline().strip())
        mew = float(file.readline().strip())
        end_time = float(file.readline().strip())

    # Generate the velocity and time lists using the earlier function making sure to convert the user angle to radians
    vel_list = calc_v_over_time(math.radians(angle), mew, end_time)[0]
    time_list = calc_v_over_time(math.radians(angle), mew, end_time)[1]

    # Establish a root for the GUI and generate an app with the inputs of the 2 lists just defined
    root = tk.Tk()
    app = Blocks_on_slopes_Variable_Outputs_GUI(root, vel_list, time_list)
    root.mainloop()
