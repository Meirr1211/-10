import tkinter as tk
import random

def draw_circle(event):
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "magenta", "cyan"]
    color = random.choice(colors)
    
    r = 20  # Радиус круга
    
    # Рисуем круг в месте клика
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill=color, outline="black")

root = tk.Tk()
root.title("Тапсырма 8: Шеңбер салу")
root.geometry("600x400")  # Начальный размер окна

# Главные изменения здесь: expand=True и fill=tk.BOTH
# Это заставит белый холст растягиваться вслед за изменением размеров окна
canvas = tk.Canvas(root, bg="white", highlightthickness=1, highlightbackground="gray")
canvas.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Привязка клика мыши
canvas.bind("<Button-1>", draw_circle)

# Текст-подсказка внизу
instruction = tk.Label(root, text="Ақ алаңның ішіне тінтуірмен (мышкамен) шертіңіз", font=("Arial", 10, "italic"))
instruction.pack(pady=5)

root.mainloop()
