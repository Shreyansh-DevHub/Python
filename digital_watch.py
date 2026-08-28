import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d-%m-%Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Watch")
root.geometry("300x150")

time_label = tk.Label(root, font=("Arial", 40))
time_label.pack(pady=10)

date_label = tk.Label(root, font=("Arial", 15))
date_label.pack()

update_time()
root.mainloop()
