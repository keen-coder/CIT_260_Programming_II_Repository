# This program displays an empty window.

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Display a title.
        self.main_window.title('My First GUI')

        # Enter the tkinter main loop.
        tk.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()