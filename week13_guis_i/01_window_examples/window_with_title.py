# This program displays an empty window.

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Display a title.
        self.main_window.title('My First GUI')

        self.main_window.geometry('300x500')

        # Make the window 85% transparent
        self.main_window.attributes(alpha=0.85)

        # Enter the tkinter main loop.
        tk.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()