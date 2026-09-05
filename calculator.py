import tkinter as tk

def click(char):
    if char == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for b in buttons:
    tk.Button(root, text=b, width=5, height=2, command=lambda x=b: click(x)).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
