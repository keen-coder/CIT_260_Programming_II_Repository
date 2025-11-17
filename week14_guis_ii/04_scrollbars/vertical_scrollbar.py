# This program demonstrates a Listbox with a vertical scrollbar.
import tkinter as tk

class VerticalScrollbarExample:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()

        # Create a frame for the Listbox and vertical scrollbar.
        self.listbox_frame = tk.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        # Create a Listbox widget in the listbox_frame.
        self.listbox = tk.Listbox(
            self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')
        
        # Create a vertical Scrollbar in the listbox_frame.
        self.scrollbar = tk.Scrollbar(
            self.listbox_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side='right', fill=tk.Y)

        # Configure the Scrollbar and Listbox to work together.
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Create a list with the names of the months.
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September', 
                  'October', 'November', 'December']

        # Populate the Listbox with the data.
        for month in months:
            self.listbox.insert(tk.END, month)

        # Start the main loop.
        tk.mainloop()

# Create an instance of the VerticalScrollbarExample class.
if __name__ == '__main__':
    scrollbar_example = VerticalScrollbarExample()