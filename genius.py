import random
import tkinter as tk
from tkinter import messagebox
import time

class SimonSaysGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Simon Says Game")
        self.master.geometry("300x200")

        self.colors = ["Red", "Blue", "Green", "Yellow"]
        self.sequence = []
        self.user_sequence = []
        self.level = 1

        self.create_widgets()
        self.generate_sequence()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Repeat the sequence:")
        self.info_label.pack()

        self.color_buttons = []
        for color in self.colors:
            button = tk.Button(self.master, text=color, bg=color, width=10, height=2, command=lambda c=color: self.select_color(c))
            button.pack()
            self.color_buttons.append(button)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_sequence)
        self.submit_button.pack()

    def generate_sequence(self):
        self.sequence = [random.randint(0, 3) for _ in range(self.level)]
        self.display_sequence()

    def display_sequence(self):
        for color_index in self.sequence:
            color = self.colors[color_index]
            self.master.after(1000, self.highlight_color, color)
            self.master.after(2000, self.restore_colors)

    def highlight_color(self, color):
        for button in self.color_buttons:
            if button.cget("bg") == color:
                button.config(bg="white")
                self.master.update()
                time.sleep(1)

    def restore_colors(self):
        for button in self.color_buttons:
            button.config(bg=button.cget("text"))

    def select_color(self, color):
        color_index = self.colors.index(color)
        self.user_sequence.append(color_index)

    def check_sequence(self):
        if self.sequence == self.user_sequence:
            messagebox.showinfo("Result", "Correct!")
            self.level += 1
            self.user_sequence = []
            self.generate_sequence()
        else:
            messagebox.showerror("Result", "Incorrect! Game Over!")
            self.master.destroy()

def main():
    root = tk.Tk()
    game = SimonSaysGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

