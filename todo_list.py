import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Type something first")
        return
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        if not task.startswith("[Done] "):
            listbox.delete(selected)
            listbox.insert(selected, "[Done] " + task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first")

root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=2)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Mark Done", command=mark_done).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_task).grid(row=0, column=1, padx=5)

root.mainloop()
