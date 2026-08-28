import tkinter as tk

running = False
count = 0

def start():
    global running
    running = True
    update()

def stop():
    global running
    running = False

def reset():
    global count
    count = 0
    label.config(text="00:00:00")

def update():
    global count
    if running:
        count += 1
        mins = count // 600
        secs = (count // 10) % 60
        ms = (count % 10) * 10
        label.config(text=f"{mins:02d}:{secs:02d}:{ms:02d}")
        root.after(100, update)

root = tk.Tk()
root.title("Stopwatch")
root.geometry("250x150")

label = tk.Label(root, text="00:00:00", font=("Arial", 30))
label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Start", command=start, width=8).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Stop", command=stop, width=8).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Reset", command=reset, width=8).grid(row=0, column=2, padx=5)

root.mainloop()
