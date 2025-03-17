import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.configure(bg="#2C3E50")  # Dark background
        self.root.resizable(False, False)

        # Entry field styling
        self.entry = tk.Entry(root, width=35, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('DEL', 5, 2), ('CE', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=8, height=2, font=("Arial", 14), bg="#34495E", fg="white",
                               relief="ridge", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)

        func_buttons = [
            ('π', 6, 0), ('exp', 6, 1), ('ln', 6, 2), ('log', 6, 3),
            ('sqrt', 7, 0), ('x^2', 7, 1), ('x^3', 7, 2), ('1/x', 7, 3),
            ('|x|', 8, 0), ('sin', 8, 1), ('cos', 8, 2), ('tan', 8, 3),
            ('sec', 9, 0), ('csc', 9, 1), ('cot', 9, 2), ('x^y', 9, 3),
            ('x^(1/3)', 10, 0), ('+/-', 10, 1)
        ]

        for (text, row, col) in func_buttons:
            button = tk.Button(root, text=text, width=8, height=2, font=("Arial", 14), bg="#16A085", fg="white",
                               relief="ridge", command=lambda t=text: self.on_function_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)

        # First Calculate Button
        self.calc_button1 = tk.Button(root, text="Calculate", width=35, height=2, font=("Arial", 14), bg="#E74C3C",
                                     fg="white", relief="ridge", command=self.calculate)
        self.calc_button1.grid(row=11, column=0, columnspan=4, padx=5, pady=5)

        # Second Calculate Button
        self.calc_button2 = tk.Button(root, text="Calculate", width=35, height=2, font=("Arial", 14), bg="#E74C3C",
                                     fg="white", relief="ridge", command=self.calculate)
        self.calc_button2.grid(row=12, column=0, columnspan=4, padx=5, pady=5)

    def on_button_click(self, text):
        if text == '=':
            self.calculate()
        elif text == 'DEL':
            self.delete_last_char()
        elif text == 'CE':
            self.clear_entry()
        else:
            self.entry.insert(tk.END, text)

    def on_function_click(self, text):
        if text == 'π':
            self.entry.insert(tk.END, str(math.pi))
        elif text == 'exp':
            self.entry.insert(tk.END, "math.exp(")
        elif text == 'ln':
            self.entry.insert(tk.END, "math.log(")
        elif text == 'log':
            self.entry.insert(tk.END, "math.log10(")
        elif text == 'sqrt':
            self.entry.insert(tk.END, "math.sqrt(")
        elif text == 'x^2':
            self.entry.insert(tk.END, "**2")
        elif text == 'x^3':
            self.entry.insert(tk.END, "**3")
        elif text == '1/x':
            self.entry.insert(tk.END, "1/")
        elif text == '|x|':
            self.entry.insert(tk.END, "abs(")
        elif text == 'sin':
            self.entry.insert(tk.END, "math.sin(")
        elif text == 'cos':
            self.entry.insert(tk.END, "math.cos(")
        elif text == 'tan':
            self.entry.insert(tk.END, "math.tan(")
        elif text == 'sec':
            self.entry.insert(tk.END, "1/math.cos(")
        elif text == 'csc':
            self.entry.insert(tk.END, "1/math.sin(")
        elif text == 'cot':
            self.entry.insert(tk.END, "1/math.tan(")
        elif text == 'x^y':
            self.entry.insert(tk.END, "**")
        elif text == 'x^(1/3)':
            self.entry.insert(tk.END, "**(1/3)")
        elif text == '+/-':
            current_text = self.entry.get()
            if current_text.startswith('-'):
                self.entry.delete(0, 1)
            else:
                self.entry.insert(0, "-")

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression, {"math": math, "__builtins__": {}})
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input or syntax error")

    def clear_entry(self):
        """Clear the entry field (CE button)."""
        self.entry.delete(0, tk.END)

    def delete_last_char(self):
        """Delete the last character from the entry field (DEL button)."""
        current_text = self.entry.get()
        if current_text:
            self.entry.delete(len(current_text) - 1, tk.END)

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
