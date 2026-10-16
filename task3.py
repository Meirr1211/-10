import tkinter as tk

def text_on():
    label.config(text="Мәтін пайда болды")

def text_off():
    label.config(text="")

root = tk.Tk()
root.title("Тапсырма 3")
root.geometry("300x200")

btn_on = tk.Button(root, text="Қосу", command=text_on)
btn_on.pack(side=tk.LEFT, padx=40, pady=20)

btn_off = tk.Button(root, text="Өшіру", command=text_off)
btn_off.pack(side=tk.RIGHT, padx=40, pady=20)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(side=tk.BOTTOM, pady=40)

root.mainloop()
