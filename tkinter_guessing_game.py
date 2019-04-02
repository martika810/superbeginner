import tkinter as tk
import random

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.secret_number = random.randint(1,11)

        self.label = tk.Label(self,text="Try to guess the secret number. Enter a number below:")
        self.label.pack(fill=tk.BOTH,expand = 1,padx=100,pady=50)

        self.user_number = tk.IntVar()
        self.user_number_box = tk.Entry(self, textvar=self.user_number)
        self.user_number_box.pack(fill=tk.BOTH,expand = 1,padx=100,pady=50)

        self.result_label = tk.Label(self, text = "")

        submit_button = tk.Button(self,text="Submit",command=self.check_entered_number)
        submit_button.pack(fill=tk.BOTH,expand = 1,padx=100,pady=50)


    def check_entered_number(self):
        if(self.secret_number>self.user_number.get()):
            self.result_label = tk.Label(self, text = "The secret number is larger")
        elif(self.secret_number<self.user_number.get()):
            self.result_label = tk.Label(self, text = "The secret number is larger")
        else:
            self.result_label = tk.Label(self, text = "Correct!!")
        self.result_label.pack(fill=tk.BOTH,expand = 1,padx=100,pady=50)

if __name__ == "__main__":
    window = GameWindow()
    window.mainloop()