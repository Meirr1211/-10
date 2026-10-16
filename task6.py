import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Қосындысы: {num1 + num2}")
    except ValueError:
        result_label.config(text="Қате! Сан енгізіңіз.")

root = tk.Tk()
root.title("Тапсырма 6")
root.geometry("300x200")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

btn = tk.Button(root, text="Қосу", command=add_numbers)
btn.pack(pady=10)

result_label = tk.Label(root, text="Қосындысы: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
