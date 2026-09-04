import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

folder_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

def browse_folder():
    path = filedialog.askdirectory()
    if path:
        folder_label.config(text=path)
        selected["path"] = path

def organize():
    path = selected.get("path")
    if not path:
        messagebox.showwarning("Warning", "Select a folder first")
        return

    moved = 0
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            ext = os.path.splitext(filename)[1].lower()
            target_folder = "Others"

            for folder_name, extensions in folder_types.items():
                if ext in extensions:
                    target_folder = folder_name
                    break

            dest_dir = os.path.join(path, target_folder)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.move(full_path, os.path.join(dest_dir, filename))
            moved += 1

    messagebox.showinfo("Done", f"Organized {moved} files")

selected = {}

root = tk.Tk()
root.title("Folder Organizer")
root.geometry("400x180")

tk.Button(root, text="Select Folder", command=browse_folder).pack(pady=10)

folder_label = tk.Label(root, text="No folder selected", wraplength=350)
folder_label.pack(pady=10)

tk.Button(root, text="Organize Now", command=organize).pack(pady=10)

root.mainloop()
