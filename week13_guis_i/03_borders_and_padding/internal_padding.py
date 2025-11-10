# This program demonstrates internal padding.
import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tk.Tk()

        # Create two Label widgets with solid borders.
        self.label1 = tk.Label(self.main_window,
                                    text='Hello World!',
                                    borderwidth=1,
                                    relief='solid')
                                    
        self.label2 = tk.Label(self.main_window,
                         text='This is my GUI program.',
                         borderwidth=1,
                         relief='solid')

        # Display the Labels with 20 pixels of horizontal
        # and vertical internal padding.
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)

        # Enter the tkinter main loop.
        tk.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()