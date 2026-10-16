import tkinter as tk

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    result_label.config(text=f"Пайдаланушы: {name}\nЖасы: {age}-да")

root = tk.Tk()
root.title("Тапсырма 10")
root.geometry("350x250")

# Аты-жөні
tk.Label(root, text="Аты-жөніңіз:").pack(pady=2)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Жасы
tk.Label(root, text="Жасыңыз:").pack(pady=2)
entry_age = tk.Entry(root, width=10)
entry_age.pack(pady=5)

# Батырма
btn_submit = tk.Button(root, text="Жіберу", command=submit_form, bg="lightblue")
btn_submit.pack(pady=15)

# Нәтиже шығаратын орын
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
