import tkinter as tk
def create_gui():
    root = tk.Tk()
    root.title("Simple GUI")

    label = tk.Label(root, text="Hello, World!")
    label.pack()

    button = tk.Button(root, text="Click Me", command=root.quit)
    button.pack()

    root.mainloop()

create_gui()