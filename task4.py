import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 4")

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# Тікбұрыш (қызыл)
canvas.create_rectangle(20, 50, 120, 150, fill="red")

# Шеңбер (жасыл)
canvas.create_oval(150, 50, 250, 150, fill="green")

# Үшбұрыш (көк)
canvas.create_polygon(330, 50, 280, 150, 380, 150, fill="blue")

root.mainloop()
