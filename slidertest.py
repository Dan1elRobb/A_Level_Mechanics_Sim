import time
import tkinter as tk

tk = tk.Tk()

###

def everysecond():
    print("One second has passed.")
    # Put here the code to reduce the tkinter counter by one.
    # For example, modify the label.

###

secs = int(time.time())

while True:
    tk.update()
    tk.update_idletasks()

    if int(time.time()) > secs:
        secs = int(time.time())
        everysecond()