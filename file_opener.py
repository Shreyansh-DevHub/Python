import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys

def browse_file():
    path = filedialog.askopenfilename()
    if path:
        path_label.config(text=path)
        selected_file["path"] = path

def open_file():
    path = selected_file.get("path")
    if not path:
        path_label.config(text="No file selected!")
        return

    # open with whatever the OS default program is
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform.startswith("darwin"):
        subprocess.call(["open", path])
    else:
        subprocess.call(["xdg-open", path])

selected_file = {}

root = tk.Tk()
root.title("File Opener")
root.geometry("400x150")

tk.Button(root, text="Browse File", command=browse_file).pack(pady=10)

path_label = tk.Label(root, text="No file selected", wraplength=350)
path_label.pack(pady=10)

tk.Button(root, text="Open File", command=open_file).pack(pady=10)

root.mainloop()
