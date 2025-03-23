import tkinter as tk
import random

class Mastermind:
    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind Game")
        self.master.config(bg="#f0f0f0")  # Set background color
        
        # Colors list
        self.colors = ['Red', 'Green', 'Blue', 'Yellow', 'Magenta', 'Cyan']
        self.color_hex = {'Red': '#FF6347', 'Green': '#32CD32', 'Blue': '#1E90FF', 'Yellow': '#FFD700', 
                          'Magenta': '#FF00FF', 'Cyan': '#00FFFF'}  
        self.secret_code = [random.choice(self.colors) for _ in range(4)]
        self.attempts, self.max_attempts = 0, 13
        
        self.create_widgets()

    def create_widgets(self):
        # Header label
        self.header_label = tk.Label(self.master, text="Welcome to Mastermind!", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.header_label.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Instructions text
        self.instruction_label = tk.Label(self.master, text="Enter your guess (4 colors):", font=("Arial", 12), bg="#f0f0f0")
        self.instruction_label.grid(row=1, column=0, columnspan=4)
        
        # User guess entry boxes
        self.guess_entries = [tk.Entry(self.master, width=10, font=("Arial", 14)) for _ in range(4)]
        for i, entry in enumerate(self.guess_entries):
            entry.grid(row=2, column=i, padx=10)
        
        # Color selection buttons
        self.color_buttons = [tk.Button(self.master, text=color, bg=self.color_hex[color], width=10, command=lambda c=color: self.set_color(c)) for color in self.colors]
        for i, btn in enumerate(self.color_buttons):
            btn.grid(row=3, column=i, padx=10, pady=10)
        
        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.check_guess)
        self.submit_button.grid(row=4, column=0, columnspan=4, pady=20)
        
        # Result and attempts labels
        self.result_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#f0f0f0")
        self.result_label.grid(row=5, column=0, columnspan=4)
        
        # Remaining attempts label
        self.attempts_label = tk.Label(self.master, text=f"Attempts: {self.attempts}/{self.max_attempts}", font=("Arial", 12), bg="#f0f0f0")
        self.attempts_label.grid(row=6, column=0, columnspan=4)
        
        # Reset button
        self.reset_button = tk.Button(self.master, text="Restart", font=("Arial", 14), bg="#FF6347", fg="white", command=self.reset_game)
        self.reset_button.grid(row=7, column=0, columnspan=4, pady=10)
    
    def set_color(self, color):
        for entry in self.guess_entries:
            if entry.get() == "":
                entry.insert(0, color)
                break
    
    def check_guess(self):
        guess = [entry.get().capitalize() for entry in self.guess_entries]
        if len(guess) != 4 or any(color not in self.colors for color in guess): 
            return self.result_label.config(text="Invalid colors. Please enter valid colors.", fg="red")
        
        correct_position = sum(g == s for g, s in zip(guess, self.secret_code))
        correct_color = sum(min(guess.count(c), self.secret_code.count(c)) for c in self.colors) - correct_position
        
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        if correct_position == 4:
            self.result_label.config(text=f"Congratulations! You guessed correctly in {self.attempts} attempts.", fg="green")
        elif self.attempts < self.max_attempts:
            self.result_label.config(text=f"{correct_position} correct positions, {correct_color} correct colors.", fg="orange")
        else:
            self.result_label.config(text=f"Sorry, the secret code was: {', '.join(self.secret_code)}", fg="red")
        
        if self.attempts >= self.max_attempts or correct_position == 4:
            self.submit_button.config(state="disabled")
        
        # Clear guess entries after each attempt
        for entry in self.guess_entries:
            entry.delete(0, tk.END)

    def reset_game(self):
        self.secret_code = [random.choice(self.colors) for _ in range(4)]
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.result_label.config(text="")
        for entry in self.guess_entries:
            entry.delete(0, tk.END)
        self.submit_button.config(state="normal")

# Create main window
root = tk.Tk()
game = Mastermind(root)
root.mainloop()
