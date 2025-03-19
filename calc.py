import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Variables to store inputs
        self.first_number = tk.StringVar()
        self.second_number = tk.StringVar()
        self.result = tk.StringVar()
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        title_label = tk.Label(
            self.root,
            text="Calculator",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=10)
        
        # Create main frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=10, padx=20, fill="both")
        
        # First number input
        tk.Label(
            main_frame,
            text="First Number:",
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w"
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        entry1 = tk.Entry(
            main_frame,
            textvariable=self.first_number,
            font=("Arial", 12),
            bd=2,
            relief=tk.GROOVE
        )
        entry1.grid(row=0, column=1, pady=5, padx=5, sticky="we")
        
        # Second number input
        tk.Label(
            main_frame,
            text="Second Number:",
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w"
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        entry2 = tk.Entry(
            main_frame,
            textvariable=self.second_number,
            font=("Arial", 12),
            bd=2,
            relief=tk.GROOVE
        )
        entry2.grid(row=1, column=1, pady=5, padx=5, sticky="we")
        
        # Operation frame
        op_frame = tk.LabelFrame(
            main_frame,
            text="Operation",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        op_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="we")
        
        # Operation buttons
        operations = [
            ("+", "Addition"),
            ("-", "Subtraction"),
            ("*", "Multiplication"),
            ("/", "Division"),
            ("**", "Power"),
            ("%", "Modulus")
        ]
        
        self.operations_frame = tk.Frame(op_frame, bg="#f0f0f0")
        self.operations_frame.pack(pady=5, fill="both")
        
        for i, (op, text) in enumerate(operations):
            row, col = divmod(i, 3)
            tk.Button(
                self.operations_frame,
                text=text,
                font=("Arial", 10),
                width=12,
                bg="#e0e0e0",
                command=lambda operation=op: self.calculate(operation)
            ).grid(row=row, column=col, padx=5, pady=5)
        
        # Result frame
        result_frame = tk.Frame(main_frame, bg="#f0f0f0")
        result_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")
        
        tk.Label(
            result_frame,
            text="Result:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(pady=5)
        
        result_label = tk.Label(
            result_frame,
            textvariable=self.result,
            font=("Arial", 14),
            bg="white",
            relief=tk.SUNKEN,
            height=2,
            width=25
        )
        result_label.pack(pady=5, fill="x")
        
        # Clear button
        clear_button = tk.Button(
            main_frame,
            text="Clear",
            font=("Arial", 12),
            bg="#ff6b6b",
            fg="white",
            command=self.clear_inputs
        )
        clear_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")
    
    def calculate(self, operation):
        try:
            num1 = float(self.first_number.get())
            num2 = float(self.second_number.get())
            
            if operation == '+':
                result = num1 + num2
                symbol = '+'
            elif operation == '-':
                result = num1 - num2
                symbol = '-'
            elif operation == '*':
                result = num1 * num2
                symbol = '×'
            elif operation == '/':
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2
                symbol = '÷'
            elif operation == '**':
                result = num1 ** num2
                symbol = '^'
            elif operation == '%':
                result = num1 % num2
                symbol = '%'
            
            # Format the result to remove trailing zeros if it's a whole number
            if result == int(result):
                result = int(result)
                
            self.result.set(f"{num1} {symbol} {num2} = {result}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def clear_inputs(self):
        self.first_number.set("")
        self.second_number.set("")
        self.result.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()