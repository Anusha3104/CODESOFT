import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Game variables
        self.choices = ['rock', 'paper', 'scissors']
        self.scores = {'user': 0, 'computer': 0}
        
        # UI Setup
        self.setup_ui()
    
    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(
            main_frame,
            text="Rock-Paper-Scissors",
            font=('Helvetica', 18, 'bold')
        ).pack(pady=10)
        
        # Instructions
        ttk.Label(
            main_frame,
            text="Choose your move:",
            font=('Helvetica', 12)
        ).pack(pady=10)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=10)
        
        # Choice Buttons
        ttk.Button(
            buttons_frame,
            text="✊ Rock",
            command=lambda: self.play_game('rock')
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            buttons_frame,
            text="✋ Paper",
            command=lambda: self.play_game('paper')
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            buttons_frame,
            text="✌️ Scissors",
            command=lambda: self.play_game('scissors')
        ).pack(side=tk.LEFT, padx=10)
        
        # Results Frame
        results_frame = ttk.LabelFrame(main_frame, text="Game Results", padding=10)
        results_frame.pack(fill=tk.X, pady=10)
        
        self.user_choice_label = ttk.Label(results_frame, text="Your choice: -", font=('Helvetica', 10))
        self.user_choice_label.pack()
        
        self.computer_choice_label = ttk.Label(results_frame, text="Computer choice: -", font=('Helvetica', 10))
        self.computer_choice_label.pack()
        
        self.result_label = ttk.Label(results_frame, text="", font=('Helvetica', 12, 'bold'))
        self.result_label.pack(pady=5)
        
        # Scores Frame
        scores_frame = ttk.Frame(main_frame)
        scores_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(scores_frame, text="Scores:", font=('Helvetica', 10)).pack()
        
        self.scores_label = ttk.Label(
            scores_frame,
            text="You: 0 | Computer: 0",
            font=('Helvetica', 10, 'bold')
        )
        self.scores_label.pack()
    
    def play_game(self, user_choice):
        computer_choice = random.choice(self.choices)
        
        # Update choice labels
        self.user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice.capitalize()}")
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
            color = "blue"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            result = "You win! 🎉"
            color = "green"
            self.scores['user'] += 1
        else:
            result = "Computer wins! 😢"
            color = "red"
            self.scores['computer'] += 1
        
        # Update result and scores
        self.result_label.config(text=result, foreground=color)
        self.scores_label.config(text=f"You: {self.scores['user']} | Computer: {self.scores['computer']}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    game.run()
