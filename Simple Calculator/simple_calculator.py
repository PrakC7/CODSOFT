import tkinter as tk
from tkinter import ttk
import math

# Handle operation selection
def select_operation(op):
    global current_op
    current_op = op
    op_label.config(text=op)

    # Show/hide second input field based on operation
    if op == '√':
        entry2.grid_remove()
    else:
        entry2.grid()

    result.set("")

# Perform the selected calculation
def calculate():
    try:
        num1 = float(entry1.get()) if entry1.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0

        if current_op == '+':
            result.set(f"Result: {num1 + num2}")
        elif current_op == '-':
            result.set(f"Result: {num1 - num2}")
        elif current_op == '×':
            result.set(f"Result: {num1 * num2}")
        elif current_op == '÷':
            if num2 == 0:
                result.set("Oops! Can't divide by 0 😬")
            else:
                result.set(f"Result: {round(num1 / num2, 5)}")
        elif current_op == '%':
            result.set(f"Result: {num1 % num2}")
        elif current_op == '^':
            result.set(f"Result: {num1 ** num2}")
        elif current_op == '√':
            if num1 < 0:
                result.set("No real square root for negative 😕")
            else:
                result.set(f"√{num1} = {round(math.sqrt(num1), 5)}")
    except ValueError:
        result.set("Enter valid numbers 🙏")

# Clear everything
def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    op_label.config(text="?")
    result.set("")
    entry2.grid()

# Setup
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("460x500")
app.configure(bg="#f7f7f7")

current_op = None

# Header
tk.Label(app, text="🧠 Simple Calculator", font=("Segoe UI Semibold", 20), bg="#f7f7f7", fg="#1e293b").pack(pady=(20, 10))

# Operation Buttons
op_frame = tk.Frame(app, bg="#f7f7f7")
op_frame.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=6)

ttk.Button(op_frame, text="+", width=6, command=lambda: select_operation('+')).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(op_frame, text="-", width=6, command=lambda: select_operation('-')).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(op_frame, text="×", width=6, command=lambda: select_operation('×')).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(op_frame, text="÷", width=6, command=lambda: select_operation('÷')).grid(row=0, column=3, padx=5, pady=5)
ttk.Button(op_frame, text="%", width=6, command=lambda: select_operation('%')).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(op_frame, text="^", width=6, command=lambda: select_operation('^')).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(op_frame, text="√", width=6, command=lambda: select_operation('√')).grid(row=1, column=2, padx=5, pady=5)

# Entry Fields and Operation Symbol Display
entry_frame = tk.Frame(app, bg="#f7f7f7")
entry_frame.pack(pady=25)

entry1 = ttk.Entry(entry_frame, font=("Segoe UI", 14), width=15)
entry1.grid(row=0, column=0, padx=5)

op_label = tk.Label(entry_frame, text="?", font=("Segoe UI", 16, "bold"), bg="#f7f7f7", fg="#111827")
op_label.grid(row=0, column=1, padx=8)

entry2 = ttk.Entry(entry_frame, font=("Segoe UI", 14), width=15)
entry2.grid(row=0, column=2, padx=5)

# Calculate & Clear Buttons
action_frame = tk.Frame(app, bg="#f7f7f7")
action_frame.pack(pady=10)

ttk.Button(action_frame, text="Calculate", command=calculate).grid(row=0, column=0, padx=8)
ttk.Button(action_frame, text="Reset", command=clear_all).grid(row=0, column=1, padx=8)

# Result Label
result = tk.StringVar()
tk.Label(app, textvariable=result, font=("Segoe UI", 15), bg="#f7f7f7", fg="#111827", wraplength=400, justify="center").pack(pady=(30, 10))

# Footer
tk.Label(app, text="Made with ❤ by Prakhar — CodSoft Task 2", font=("Segoe UI", 9), bg="#f7f7f7", fg="#6b7280").pack(pady=10)

app.mainloop()