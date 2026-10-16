import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 1")
root.geometry("300x200")

# Мәтінді орналастыру және түсін көк (blue) етіп өзгерту
label = tk.Label(root, text="Зертханалық жұмыс №10", font=("Arial", 14), fg="blue")
label.pack(pady=50)  # pady - жоғарыдан және төменнен қалдырылатын орын (позициясы)

root.mainloop()
