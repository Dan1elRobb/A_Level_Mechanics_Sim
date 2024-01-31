import tkinter as tk
import pygame
from pygame.locals import *

class PygameApp:
    def __init__(self, master, width=400, height=300):
        self.master = master
        self.master.title("Pygame in Tkinter")

        # Set up Pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # Create a Pygame surface
        self.pygame_frame = pygame.Surface((width, height))
        self.pygame_frame.fill((255, 255, 255))  # Fill with white initially

        # Create a Tkinter canvas
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack()

        # Embed Pygame surface in Tkinter canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.pygame_frame)

        # Set up Pygame animation variables
        self.x = 50
        self.y = 50

    def update_animation(self):
        # Update animation logic (e.g., move an object)
        self.x += 2
        self.y += 1

        # Draw on Pygame surface
        self.pygame_frame.fill((255, 255, 255))  # Clear the surface
        pygame.draw.circle(self.pygame_frame, (0, 0, 255), (self.x, self.y), 20)  # Draw a blue circle

    def run(self):
        # Main loop
        while True:
            self.update_animation()

            # Update Tkinter canvas
            self.canvas.update()

            # Limit frames per second
            self.clock.tick(30)

            # Handle Tkinter events
            self.master.update_idletasks()
            self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PygameApp(root)
    app.run()
