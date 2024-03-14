import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Entry for displaying the current calculation
        self.display = tk.Entry(root, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for button in buttons:
            text, row, column = button
            tk.Button(root, text=text, padx=20, pady=20, command=lambda text=text: self.button_click(text)).grid(row=row, column=column)

        # Clear button
        tk.Button(root, text='C', padx=20, pady=20, command=self.clear).grid(row=5, column=0, columnspan=4)

    def button_click(self, text):
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'C':
            self.clear()
        else:
            self.expression += text
            self.display.insert(tk.END, text)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
