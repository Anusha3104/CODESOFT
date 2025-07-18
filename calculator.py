import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Arial', 12), padding=10)
        self.style.configure("TLabel", font=('Arial', 14))
        
        # Variables
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.operation = tk.StringVar(value="+")
        self.result = tk.StringVar()
        
        # GUI Layout
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Simple Calculator", style="TLabel")
        title_label.pack(pady=10)
        
        # Number Inputs
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="First Number:").grid(row=0, column=0, padx=5, pady=5)
        num1_entry = ttk.Entry(input_frame, textvariable=self.num1, font=('Arial', 12))
        num1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Second Number:").grid(row=1, column=0, padx=5, pady=5)
        num2_entry = ttk.Entry(input_frame, textvariable=self.num2, font=('Arial', 12))
        num2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Operation Selection
        operation_frame = ttk.Frame(self.root)
        operation_frame.pack(pady=10)
        
        ttk.Label(operation_frame, text="Operation:").pack()
        
        operations = ["+", "-", "*", "/"]
        for op in operations:
            ttk.Radiobutton(
                operation_frame,
                text=op,
                variable=self.operation,
                value=op
            ).pack(side=tk.LEFT, padx=5)
        
        # Calculate Button
        calculate_btn = ttk.Button(
            self.root,
            text="Calculate",
            command=self.calculate
        )
        calculate_btn.pack(pady=20)
        
        # Result Display
        result_frame = ttk.Frame(self.root)
        result_frame.pack(pady=10)
        
        ttk.Label(result_frame, text="Result:").pack()
        result_label = ttk.Label(
            result_frame,
            textvariable=self.result,
            font=('Arial', 16, 'bold'),
            foreground="blue"
        )
        result_label.pack()
    
    def calculate(self):
        try:
            n1 = float(self.num1.get())
            n2 = float(self.num2.get())
            op = self.operation.get()
            
            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            elif op == "*":
                res = n1 * n2
            elif op == "/":
                if n2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                res = n1 / n2
            else:
                messagebox.showerror("Error", "Invalid operation!")
                return
            
            self.result.set(f"{n1} {op} {n2} = {res}")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()          
 
        
