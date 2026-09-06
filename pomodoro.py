import tkinter as tk
from tkinter import messagebox

work_time = 25 * 60
break_time = 5 * 60
time_left = work_time
running = False
on_break = False

def update_display():
    mins = time_left // 60
    secs = time_left % 60
    label.config(text=f"{mins:02d}:{secs:02d}")

def tick():
    global time_left, running, on_break
    if running:
        if time_left > 0:
            time_left -= 1
            update_display()
            root.after(1000, tick)
        else:
            if not on_break:
                messagebox.showinfo("Pomodoro", "Work session done! Take a break.")
                on_break = True
                time_left = break_time
            else:
                messagebox.showinfo("Pomodoro", "Break over! Back to work.")
                on_break = False
                time_left = work_time
            update_display()
            root.after(1000, tick)

def start():
    global running
    running = True
    tick()

def pause():
    global running
    running = False

def reset():
    global time_left, running, on_break
    running = False
    on_break = False
    time_left = work_time
    update_display()

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("250x180")

label = tk.Label(root, text="25:00", font=("Arial", 30))
label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Start", command=start, width=7).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Pause", command=pause, width=7).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Reset", command=reset, width=7).grid(row=0, column=2, padx=5)

root.mainloop()
