
import tkinter as tk

class MyGUI:
    def __init__(self):
        self.color = 'red'

        # Create the main window widget.
        self.main_window = tk.Tk()

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tk.Button(self.main_window,
                                        text='Click Me!',
                                        command=self.change_color)

        # Pack the Button.
        self.my_button.pack()
        
        # Enter the tkinter main loop.
        tk.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    
    def change_color(self):
        if self.color == 'red':
            self.my_button.config(bg='green')
            self.color = 'green'
        else:
            self.my_button.config(bg='red')
            self.color = 'red'
            
        

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()