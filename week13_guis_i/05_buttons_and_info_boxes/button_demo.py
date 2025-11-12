# This program demonstrates a Button widget.
# When the user clicks the Button, an
# info dialog box is displayed.

import tkinter as tk
import tkinter.messagebox as tkmsg

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tk.Button(self.main_window,
                                text='Click Me!',
                                command=self.do_something)

        # Pack the Button.
        self.my_button.pack()
        
        # Enter the tkinter main loop.
        tk.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # Display an info dialog box.
       tkmsg.showinfo('Response', 'Thanks for clicking the button.')

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()