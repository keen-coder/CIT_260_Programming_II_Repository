import tkinter as tk

root = tk.Tk()

# Create a StringVar
string_var = tk.StringVar()

string_var.set("Hello, Tkinter!") # Set an initial value (optional)

# Create a Label and associate it with the StringVar
label = tk.Label(root, textvariable=string_var)
label.pack()

# Function to update the label text
def update_label():
    string_var.set("Text updated!")

# Create a Button to trigger the update
button = tk.Button(root, text="Update Text", command=update_label)
button.pack()

root.mainloop()