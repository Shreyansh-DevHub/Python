import tkinter as tk
import calendar

current_year = 2026
current_month = 8

def show_calendar():
    for widget in cal_frame.winfo_children():
        widget.destroy()

    header.config(text=f"{calendar.month_name[current_month]} {current_year}")

    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for i, d in enumerate(days):
        tk.Label(cal_frame, text=d, width=4, font=("Arial", 10, "bold")).grid(row=0, column=i)

    month_days = calendar.monthcalendar(current_year, current_month)
    for row_num, week in enumerate(month_days, start=1):
        for col_num, day in enumerate(week):
            text = str(day) if day != 0 else ""
            tk.Label(cal_frame, text=text, width=4).grid(row=row_num, column=col_num)

def next_month():
    global current_month, current_year
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    show_calendar()

def prev_month():
    global current_month, current_year
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    show_calendar()

root = tk.Tk()
root.title("Calendar")
root.geometry("300x250")

nav_frame = tk.Frame(root)
nav_frame.pack(pady=5)

tk.Button(nav_frame, text="<", command=prev_month).grid(row=0, column=0)
header = tk.Label(nav_frame, text="", font=("Arial", 14))
header.grid(row=0, column=1, padx=20)
tk.Button(nav_frame, text=">", command=next_month).grid(row=0, column=2)

cal_frame = tk.Frame(root)
cal_frame.pack(pady=10)

show_calendar()
root.mainloop()
