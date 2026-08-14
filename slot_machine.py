import tkinter as tk
import random


symbols = ["🍒", "🍋", "🔔", "⭐", "💎", "7"]

payouts = {
    "🍒": 3,
    "🍋": 5,
    "🔔": 8,
    "⭐": 15,
    "💎": 30,
    "7": 100
}


odds = {
    "🍒": 30,
    "🍋": 25,
    "🔔": 20,
    "⭐": 15,
    "💎": 7,
    "7": 3
}


cost_per_spin = 10
start_balance = 500
num_reels = 3
spin_steps = 14 
spin_delay = 60 


bg_color = "#1b1025"
bg_color_2 = "#2b1a3d"
reel_bg = "#f4e9d8"
gold = "#ffcc4d"
gold_dark = "#e0a800"
green = "#3ddc84"
red = "#ff6b6b"
white = "#f5f0ff"
gray = "#c9b8dd"


weighted_list = []
for sym in odds:
    weight = odds[sym]
    for i in range(weight):
        weighted_list.append(sym)

class SlotMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Slot Machine")
        self.configure(bg=bg_color)
        self.resizable(False, False)

        self.balance = start_balance
        self.is_spinning = False

        self.setup_ui()

    def setup_ui(self):
      
        main_frame = tk.Frame(self, bg=bg_color)
        main_frame.pack(padx=25, pady=20)

        title_lbl = tk.Label(main_frame, text="SLOT MACHINE", font=("Georgia", 22, "bold"), bg=bg_color, fg=gold)
        title_lbl.pack(pady=(0, 15))

       
        machine_frame = tk.Frame(main_frame, bg=bg_color_2, highlightthickness=3, highlightbackground=gold)
        machine_frame.pack(pady=(0, 15), ipadx=10, ipady=14)

        reels_container = tk.Frame(machine_frame, bg=bg_color_2)
        reels_container.pack(pady=6, padx=6)
        
        self.reel_labels = []
    
        for i in range(num_reels):
            lbl = tk.Label(reels_container, text="?", width=3, height=1, font=("Segoe UI Emoji", 30), bg=reel_bg, fg="#222222", relief="flat")
            lbl.grid(row=0, column=i, padx=8, pady=4)
            self.reel_labels.append(lbl)

        self.balance_var = tk.StringVar()
        self.balance_var.set("Credits: " + str(self.balance))
        bal_lbl = tk.Label(main_frame, textvariable=self.balance_var, font=("Segoe UI", 16, "bold"), bg=bg_color, fg=white)
        bal_lbl.pack(pady=(4, 2))

        
        self.status_var = tk.StringVar()
        self.status_var.set("Press SPIN to play")
        self.status_lbl = tk.Label(main_frame, textvariable=self.status_var, wraplength=300, font=("Segoe UI", 11), bg=bg_color, fg=gray)
        self.status_lbl.pack(pady=10)

     
        btn_frame = tk.Frame(main_frame, bg=bg_color)
        btn_frame.pack(pady=10)

        self.spin_btn = tk.Button(btn_frame, text="SPIN", command=self.handle_spin, font=("Segoe UI", 11, "bold"), bg=gold, fg="#2b1a3d", activebackground=gold_dark, relief="flat", padx=18, pady=8)
        self.spin_btn.grid(row=0, column=0, padx=5)

        reset_btn = tk.Button(btn_frame, text="Reset Credits", command=self.reset_balance, font=("Segoe UI", 11, "bold"), bg=bg_color_2, fg=white, activebackground="#3d254f", relief="flat", padx=14, pady=8)
        reset_btn.grid(row=0, column=1, padx=5)

        
        payout_text = "Payouts:\n"
        for s in symbols:
            payout_text = payout_text + s + " x" + str(payouts[s]) + "   "
        
        info_lbl = tk.Label(main_frame, text=payout_text, justify="left", bg=bg_color, fg=gray, font=("Segoe UI", 10))
        info_lbl.pack(pady=10)

    def reset_balance(self):
        if self.is_spinning:
            return
        self.balance = start_balance
        self.balance_var.set("Credits: " + str(self.balance))
        self.status_var.set("Credits reset.")
        self.status_lbl.config(fg=gray)

    def handle_spin(self):
       
        if self.is_spinning:
            return

        if self.balance < cost_per_spin:
            self.status_var.set("Not enough credits!")
            self.status_lbl.config(fg=red)
            return

        self.is_spinning = True
        self.spin_btn.config(state="disabled")
        
        
        self.balance -= cost_per_spin
        self.balance_var.set("Credits: " + str(self.balance))
        self.status_var.set("Spinning...")
        

        self.run_animation(0)

    def run_animation(self, step):
        if step < spin_steps:
            
            for lbl in self.reel_labels:
                lbl.config(text=random.choice(symbols))
            
           
            self.after(spin_delay, lambda: self.run_animation(step + 1))
        else:
            self.finish_spin()

    def finish_spin(self):
       
        final_results = []
        for _ in range(num_reels):
            final_results.append(random.choice(weighted_list))

       
        for i in range(len(self.reel_labels)):
            self.reel_labels[i].config(text=final_results[i])

        # Calculate winnings
        win_amount, message = self.calculate_winnings(final_results)
        
        self.balance += win_amount
        self.balance_var.set("Credits: " + str(self.balance))
        self.status_var.set(message)
        
        if win_amount > 0:
            self.status_lbl.config(fg=green)
        else:
            self.status_lbl.config(fg=gray)
            
        self.is_spinning = False
        self.spin_btn.config(state="normal")

    def calculate_winnings(self, results):
        
        if results[0] == results[1] == results[2]:
            symbol = results[0]
            winnings = cost_per_spin * payouts[symbol]
            return winnings, "JACKPOT! Three " + symbol + "s!"
        
       
        if results[0] == results[1] or results[1] == results[2] or results[0] == results[2]:
            winnings = int(cost_per_spin * 1.5)
            return winnings, "Nice! Two matching symbols."
            
        return 0, "No match this time."

if __name__ == "__main__":
    app = SlotMachine()
    app.mainloop()