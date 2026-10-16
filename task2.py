import tkinter as tk

def show_message():
    label.config(text="Сәлем, Python!")

root = tk.Tk()
root.title("Тапсырма 2")
root.geometry("300x200")

button = tk.Button(root, text="Басыңыз", command=show_message)
button.pack(pady=20)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
