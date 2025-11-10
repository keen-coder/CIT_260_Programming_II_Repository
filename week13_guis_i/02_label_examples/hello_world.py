# This program displays a label with text.

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Create a Label widget containing the
        # text 'Hello World!'
        self.label = tk.Label(self.main_window,
                                   text='Hello World!')

        # Call the Label widget's pack method.
        self.label.pack()

        # Enter the tkinter main loop.
        tk.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()