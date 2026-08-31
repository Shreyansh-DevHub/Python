import tkinter as tk
from tkinter import messagebox

subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
entries = []

def calculate():
    try:
        marks = [float(e.get()) for e in entries]
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers in all fields")
        return

    total = sum(marks)
    percentage = total / (len(marks) * 100) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    result_label.config(text=f"Total: {total}/{len(marks)*100}   Percentage: {percentage:.2f}%   Grade: {grade}")

root = tk.Tk()
root.title("Result Calculator")
root.geometry("350x350")

tk.Label(root, text="Enter marks out of 100", font=("Arial", 12)).pack(pady=10)

for sub in subjects:
    frame = tk.Frame(root)
    frame.pack(pady=3)
    tk.Label(frame, text=sub, width=12, anchor="w").pack(side=tk.LEFT)
    e = tk.Entry(frame, width=10)
    e.pack(side=tk.LEFT)
    entries.append(e)

tk.Button(root, text="Calculate", command=calculate).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 10), wraplength=300)
result_label.pack(pady=10)

root.mainloop()
