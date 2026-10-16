import tkinter as tk

def change_color(selected_color):
    root.config(bg=selected_color)
    label.config(bg=selected_color)

root = tk.Tk()
root.title("Тапсырма 5")
root.geometry("300x200")

label = tk.Label(root, text="Түсті таңдаңыз:", font=("Arial", 12))
label.pack(pady=10)

colors = ["white", "lightblue", "lightgreen", "yellow", "pink"]
current_color = tk.StringVar()
current_color.set(colors[0])

# Таңдау мәзірі (OptionMenu)
dropdown = tk.OptionMenu(root, current_color, *colors, command=change_color)
dropdown.pack(pady=10)

root.mainloop()
