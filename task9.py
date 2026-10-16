import tkinter as tk

def display_text():
    user_text = entry.get()
    label_output.config(text=user_text)

root = tk.Tk()
root.title("Тапсырма 9")
root.geometry("350x200")

entry = tk.Entry(root, width=30)
entry.pack(pady=15)

btn = tk.Button(root, text="Көрсету", command=display_text)
btn.pack(pady=10)

label_output = tk.Label(root, text="", font=("Arial", 14), fg="darkgreen")
label_output.pack(pady=15)

root.mainloop()
