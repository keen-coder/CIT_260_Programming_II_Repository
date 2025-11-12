# This program converts distances in kilometers
# to miles. The result is displayed in an info
# dialog box.

import tkinter as tk
import tkinter.messagebox as tkmsg

class KiloConverterGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()

        # Create two frames to group widgets.
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tk.Label(self.top_frame,
                    text='Enter a distance in kilometers:')
        self.kilo_entry = tk.Entry(self.top_frame,
                                        width=20)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tk.Button(self.bottom_frame,
                                          text='Convert',
                                          command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tk.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    
    def convert(self):
        # Get the value entered by the user into the
        # kilo_entry widget.
        kilo = float(self.kilo_entry.get())

        # Convert kilometers to miles.
        miles = kilo * 0.6214

        result = str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.'

        # Display the results in an info dialog box.
        tkmsg.showinfo('Results', result)

# Create an instance of the KiloConverterGUI class.
if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()