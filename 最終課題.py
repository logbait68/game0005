import tkinter as tk
import random


word_list = ["python", "tkinter", "title", "button", "label", "entry", "canvas", "__init__", "return", "print","github","mainloop","config"]

class TypingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("タイピングゲーム")
        self.time_limit = 60
        self.time_left = self.time_limit
        self.score = 0
        self.current_word = ""
        self.correct_count = 0

        self.label = tk.Label(master, text="スタートボタンを押してください")
        self.label.pack()

        self.word_label = tk.Label(master, font=('Helvetica', 24))
        self.word_label.pack()

        self.entry = tk.Entry(master, font=('Helvetica', 24))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_word)

        self.time_label = tk.Label(master, text=f"残り時間: {self.time_left}")
        self.time_label.pack()

        self.score_label = tk.Label(master, text=f"スコア: {self.score}")
        self.score_label.pack()

        self.start_button = tk.Button(master, text="スタート", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.score = 0
        self.time_left = self.time_limit
        self.correct_count = 0
        self.update_word()
        self.update_timer()
        self.start_button.config(state=tk.DISABLED)

    def update_word(self):
        self.current_word = random.choice(word_list)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)

    def check_word(self, event):
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            self.score += 3
            self.correct_count += 1
            if self.correct_count == 5:
                self.time_left += 5
                self.correct_count = 0
        else:
            self.correct_count = 0

        self.score_label.config(text=f"スコア: {self.score}")
        self.update_word()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"残り時間: {self.time_left}")
            self.master.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        if self.score > 150:
            result = "PERFECT!"
        elif self.score > 100:
            result = "GOOD!"
        elif self.score >0:
            result="bad"
        else:
            result = "終了!"
        
        self.word_label.config(text=result)
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
