import tkinter as tk
import math



class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, width=20, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4,
                          padx=10, pady=10, ipadx=10, ipady=10)

        button_list = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            ".", "0", "C", "/"
        ]

        row = 1
        col = 0
        for button in button_list:
            self.button = tk.Button(
                self, text=button, width=5, height=2, command=lambda: self.button_click(button))
            self.button.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.equal_button = tk.Button(
            self, text="=", width=5, height=2, command=self.equal_button_click)
        self.equal_button.grid(row=row, column=col,
                               columnspan=4, padx=10, pady=10)






        self.add_button = tk.Button(
            self, text="Add", width=5, height=2, command=self.add_button_click)
        self.add_button.grid(row=row+1, column=0, padx=10, pady=10)

        self.subtract_button = tk.Button(
            self, text="Subtract", width=5, height=2, command=self.subtract_button_click)
        self.subtract_button.grid(row=row+1, column=1, padx=10, pady=10)

        self.multiply_button = tk.Button(
            self, text="Multiply", width=5, height=2, command=self.multiply_button_click)
        self.multiply_button.grid(row=row+1, column=2, padx=10, pady=10)

        self.divide_button = tk.Button(
            self, text="Divide", width=5, height=2, command=self.divide_button_click)
        self.divide_button.grid(row=row+1, column=3, padx=10, pady=10)

        self.rest_div_button = tk.Button(
            self, text="Rest of division", width=13, height=2, command=self.rest_div_button_click)
        self.rest_div_button.grid(row=row+2, column=0,
