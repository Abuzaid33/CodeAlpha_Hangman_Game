import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'strawberry', 'blueberry', 'peach', 'watermelon', 'pineapple']
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = set()
        
        self.word_label = tk.Label(master, text=self.get_display_word())
        self.word_label.pack()
        
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()
        
        self.message_label = tk.Label(master, text="")
        self.message_label.pack()
        
        self.update_display()
    
    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word
    
    def guess_letter(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            self.message_label.config(text="You've already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess not in self.secret_word:
            self.guesses_left -= 1
        
        self.update_display()
        
        if self.guesses_left <= 0:
            self.message_label.config(text=f"Game over! The word was {self.secret_word}.")
            self.guess_button.config(state=tk.DISABLED)
        elif self.get_display_word() == self.secret_word:
            self.message_label.config(text="Congratulations! You've guessed the word.")
            self.guess_button.config(state=tk.DISABLED)
    
    def update_display(self):
        self.word_label.config(text=self.get_display_word())
        self.message_label.config(text=f"Guesses left: {self.guesses_left}")

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
