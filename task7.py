import tkinter as tk

seconds = 0
running = False

def count():
    global seconds, running
    if running:
        seconds += 1
        label.config(text=f"Уақыт: {seconds} сек")
        root.after(1000, count)  # 1 секунд сайын қайталау

def start_timer():
    global running
    if not running:
        running = True
        count()

def stop_timer():
    global running
    running = False

root = tk.Tk()
root.title("Тапсырма 7")
root.geometry("300x200")

label = tk.Label(root, text="Уақыт: 0 сек", font=("Arial", 16))
label.pack(pady=20)

btn_start = tk.Button(root, text="Бастау", command=start_timer, bg="lightgreen")
btn_start.pack(side=tk.LEFT, padx=40)

btn_stop = tk.Button(root, text="Тоқтату", command=stop_timer, bg="tomato")
btn_stop.pack(side=tk.RIGHT, padx=40)

root.mainloop()
