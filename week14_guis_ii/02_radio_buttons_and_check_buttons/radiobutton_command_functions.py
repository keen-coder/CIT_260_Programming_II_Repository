import tkinter as tk

def show_selection():
    print("Selected option:", selected.get())

window = tk.Tk()
window.title("Radiobutton Example")

selected = tk.StringVar()
selected.set("Option 1") # Default selection

radio1 = tk.Radiobutton(window, 
                        text="Option 1", 
                        variable=selected, 
                        value="Option 1", 
                        command=show_selection)
radio2 = tk.Radiobutton(window, 
                        text="Option 2", 
                        variable=selected, 
                        value="Option 2", 
                        command=show_selection)
radio3 = tk.Radiobutton(window, 
                        text="Option 3", 
                        variable=selected, 
                        value="Option 3", 
                        command=show_selection)

radio1.pack()
radio2.pack()
radio3.pack()

window.mainloop()

